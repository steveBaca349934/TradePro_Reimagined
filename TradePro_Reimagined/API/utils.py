from django.shortcuts import render
import re
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, date
import sys
import copy
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import  risk_models
from pypfopt import expected_returns
from pypfopt.risk_models import CovarianceShrinkage
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
from datetime import datetime, timedelta
import json
import pprint

def check_pw_is_robust(pw:str)->bool:
    """
    Checking if a password is of length 12, 
    Has two numbers in it, 
    And has a special character in it

    returns True or False
    """

    if len(pw) < 12:
        return False

    # check if there are at least two numbers in the string
    num_of_numbers = 0
    for char in pw:
        if char.isdigit():
            num_of_numbers += 1

    if num_of_numbers <= 1:
        return False

    # check if any special characters exist in the string
    special_characters = re.findall(r"[, .!?]", pw)
    if len(special_characters) < 1:
        return False


    return True


def send_email():
    pass



def scrape_web_data()->dict:

    # req = HistoricalPrices('AAPL', start_date = '2022-01-15', end_date = '2022-01-30')
    standard_poor_500 = yf.Ticker("^GSPC")
    standard_poor_500_prev_close = standard_poor_500.info.get('previousClose')

    ndaq = yf.Ticker("^IXIC")
    ndaq_prev_close = ndaq.info.get('previousClose')

    djia = yf.Ticker("^DJI")
    djia_prev_close = djia.info.get('previousClose')


    return {
        'S&P500': round(standard_poor_500_prev_close,1),
        'NASDAQ': round(ndaq_prev_close,1),
        'DJIA': round(djia_prev_close,1)
    }

def check_specific_column(intermediate_df:pd.DataFrame)->bool:
    """
    For a specific ticker
    Want to test the data column and make sure it pulls
    back enough data to make sense
    
    returns DataFrame
    """
    if len(intermediate_df) == 0:
        return False

    past_date = datetime.today() - timedelta(days=730)
    past_date_year = past_date.year


    intermediate_df['Date'] = pd.to_datetime(intermediate_df['Date'])
    
    years = intermediate_df['Date'].apply(lambda x: x.year)

    # roughly trying to check that there is data from 2 years ago 
    # in the dataframe without being too stringent
    if past_date_year not in years.unique():
        return False


    return True

def handle_specific_queryset(queryset, indice:str)->pd.DataFrame:
    """
    Given the query set and the indice
    handle logic to return data
    
    returns DataFrame
    """
    df = pd.DataFrame()
    if indice == "s_and_p_500":
        json_res = queryset[0].s_and_p_500
    elif indice == "nasdaq":
        json_res = queryset[0].nasdaq
    elif indice == "djia":
        json_res = queryset[0].djia
    
    dict_res = json.loads(json_res)

    index = 0
    for ticker in dict_res:
        dates_list = dict_res.get(ticker).get('dates')
        ticker_list = dict_res.get(ticker).get('ticker')

        data_dict = dict(zip(dates_list, ticker_list))
        # print(f" for ticker {ticker}, the data is \n {data_dict} \n")

        intermediate_df = pd.DataFrame(data_dict.items(), columns=['Date',ticker])

        # run a check to make sure that the data that Im pulling back 
        # from yahoo finance is of high enough quality to use for portfolio calculations
        if check_specific_column(intermediate_df):

            if index == 0:
                df = intermediate_df

            else:
                df = df.merge(intermediate_df, on= "Date", how="left")

            index += 1

    return df

def extract_stock_data(queryset, S_AND_P = False, NASDAQ = False, DJIA = False )->pd.DataFrame:
    """
    Queries postgress and returns data for different stock indices.
    Users can either choose S&P500 stocks, NASDAQ, DJIA. Or pick all three 
    Or some combination of all three !

    returns dataframe
    """


def extract_stock_data(queryset, S_AND_P = False, NASDAQ = False, DJIA = False )->pd.DataFrame:
    """
    Queries postgress and returns data for different stock indices.
    Users can either choose S&P500 stocks, NASDAQ, DJIA. Or pick all three 
    Or some combination of all three !

    returns dataframe
    """
    df = pd.DataFrame()
    
    if S_AND_P:

        s_and_p_res_df = handle_specific_queryset(queryset, "s_and_p_500")
        if len(df) == 0: df = s_and_p_res_df

    if NASDAQ:

        nasdaq_res_df = handle_specific_queryset(queryset, "nasdaq")
        if len(df) == 0: df = nasdaq_res_df
        else: df = df.merge(nasdaq_res_df, on = "Date", how="left")
        
    if DJIA:

        djia_res_df = handle_specific_queryset(queryset, "djia")
        if len(df) == 0: df = djia_res_df
        else: df = df.merge(djia_res_df, on = "Date", how="left")

    # some final cleanup
    for col in df.columns:
        if '_' in col:
            df.pop(col)

    df.set_index('Date',inplace=True)
    return df

def get_ticker_data(tickers:dict)->pd.DataFrame:
    """
    Given a list of stock market tickers

    Return a dataframe full of previous close data
    """

    df = pd.DataFrame()
    
    # Im trying to exclude data for any tickers that have less
    # than a full 2 years of data points
    # using google as then standard because I know that it does
    # have a full 2 years

    past_date = datetime.today() - timedelta(days=730)
    today = datetime.today()

    # max_l = len(data.DataReader("GOOGL", start=past_date, end=today, data_source='yahoo')['Adj Close'])
    max_l = len(yf.Ticker("GOOGL").history(start = past_date, end = today)['Close'])

    print(f"\n \n the max length is {max_l} \n \n ")

    index = 0
    for ticker in tickers:

        ticker_obj = yf.Ticker(ticker)
        
        data = ticker_obj.history(start = past_date, end = today)['Close']

        if len(data) == max_l:

            intermediate_df = pd.DataFrame(data)
            intermediate_df.rename(columns= {'Close':f'{ticker}'}, inplace=True)
                    
            if index == 0:
                df = intermediate_df

            else:
                df = df.join(intermediate_df)

            index += 1
        
        else:

            print(f"\n \n \n the data for {ticker} looks like: ")
            print(data)
            print("\n \n \n ")
            print(f"the length of the data is {len(data)}")
            continue

    return df



def retrieve_optimal_portfolio(ticker_df:pd.DataFrame, tickers:dict, rat:int)->dict:
    """
    Given a risk assessment score, which is a measurement
    of a client's risk tolerance

    return a dictionary of investment vehicle with percentages that their 
    portfolio should allocate to each investment vehicle 
    """
    mean = expected_returns.mean_historical_return(ticker_df)

    #TODO: if the mean return of the stock has been negative over the past 
    # 2 years, then there's no reason to keep it in the calculation
    # so drop it...
    # may need to reevaluate this later though

    for index in mean.index:
        
        if mean[index] < 0:

            mean.drop(index, axis=0, inplace=True)
            ticker_df.drop(index, axis=1, inplace=True)

    # try:
    #     sample_covar_mat = risk_models.sample_cov(ticker_df)
    # except Exception as e:
    #     print("the res of sample cov is :\n ")
    #     print(e)

    try:
        S = CovarianceShrinkage(ticker_df).ledoit_wolf()
    except Exception as e:
        print("the res of Cov Shrinkage is :\n ")
        print(e)

    ef = EfficientFrontier(mean, S , weight_bounds=(0, 1))

    # the RAT score will be used to calculate 
    # the client's intended returns 
    # the higher the RAT, the higher the 
    # expected returns
    
    ef._max_return_value = copy.deepcopy(ef)._max_return()

    these_expected_returns = 0
    if rat * .1 > ef._max_return_value:
        these_expected_returns = ef._max_return_value

    elif rat * .1 < 0:
        #we need at least 5% returns to adjust for inflation
        these_expected_returns = .05

    else:
        these_expected_returns = rat * .1


    res = ef.efficient_return(these_expected_returns)
    final_res = dict()

    for ticker, alloc in res.items():
        if alloc != 0.0:
            final_res[tickers[ticker]] = alloc

    return final_res

def retrieve_optimal_portfolio_discrete_allocations(ticker_df:pd.DataFrame, rat:int, portfolio_amount:float)->dict:
    """
    Given a risk assessment score, which is a measurement
    of a client's risk tolerance

    return a dictionary of investment vehicle with percentages that their 
    portfolio should allocate to each investment vehicle 
    """

    mean = expected_returns.mean_historical_return(ticker_df)

    # continuously cutting off the bottom 25% of financial assets
    # till we get only 40 viable financial assets
    while len(mean) > 40:
        cut_off:int = np.percentile(mean, 25)
        for index in mean.index:
            
            if mean[index] <= cut_off:

                mean.drop(index, axis=0, inplace=True)
                ticker_df.drop(index, axis=1, inplace=True)

    S = risk_models.sample_cov(ticker_df)
    # ticker_df.to_csv("output_before_error.csv", index=False)
    # S = CovarianceShrinkage(ticker_df).ledoit_wolf()

    ef = EfficientFrontier(mean,S, weight_bounds=(0, 1))
    # the RAT score will be used to calculate 
    # the client's intended returns 
    # the higher the RAT, the higher the 
    # expected returns
    ef._max_return_value = copy.deepcopy(ef)._max_return()

    these_expected_returns = 0
    if rat * .1 > ef._max_return_value:
        these_expected_returns = ef._max_return_value

    elif rat * .1 < 0:
        #we need at least 5% returns to adjust for inflation
        these_expected_returns = .05

    else:
        these_expected_returns = rat * .1

    res = ef.efficient_return(these_expected_returns)
    weights:dict = ef.clean_weights() #to clean the raw weights

    latest_prices = get_latest_prices(ticker_df)
    
    discrete_allocation = DiscreteAllocation(weights, latest_prices, total_portfolio_value=portfolio_amount )

    allocation, leftover = discrete_allocation.lp_portfolio()

    # final_res = dict()

    # for ticker, alloc in allocation.items():
    #     final_res[tickers[ticker]] = alloc

    # return final_res
    return allocation


if __name__ == '__main__':
    df = pd.read_csv("/Users/stevebaca/PycharmProjects/TradePro_Reimagined/TradePro_Reimagined/sample_data_for_development.csv")
    print(df.head())

    check_specific_column(df)

    # ticker_df = get_ticker_data(tickers)

    # # ticker_df.to_excel("ticker_df.xlsx", index=False)

    # # ticker_df = pd.read_excel("ticker_df.xlsx")

    # print(f" \n \n \n the result of tickers_df is {ticker_df} \n \n \n ")

        
    # # print(f"\n \n the portfoliio looks like {retrieve_optimal_portfolio(ticker_df, tickers, 2.5)} \n \n ")
    

    # # print(f"ticker df looks like \n \n {ticker_df.head()}")

    # # print(f"\n \n the ticker_df if we slice 5 is {ticker_df.iloc[ : , :5]} \n \n ")
    # print(retrieve_optimal_portfolio_discrete_allocations(ticker_df, tickers, 3, 50000))