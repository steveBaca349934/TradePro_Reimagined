from django.shortcuts import render
import re
import yfinance as yf
import pandas as pd
from datetime import datetime, date
import sys
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import  risk_models
from pypfopt import expected_returns

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

def scrape_stock_tickers()->list:
    """
    Uses pandas to get list of all stock tickers

    returns list of stock tickers
    """
    res = []
    payload=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    stocks = payload[0]

    tickers = stocks['Symbol'].tolist()

    return tickers

def get_ticker_data(tickers:list)->pd.DataFrame:
    """
    Given a list of stock market tickers

    Return a dataframe full of previous close data
    """

    df = pd.DataFrame()
    
    for index, ticker in enumerate(tickers[:15]):

        ticker_obj = yf.Ticker(ticker)
        
        data = ticker_obj.history(period="2y")['Close']

        intermediate_df = pd.DataFrame(data)
        intermediate_df.rename(columns= {'Close':f'{ticker}'}, inplace=True)
                
        if index == 0:
            df = intermediate_df

        else:
            df = df.join(intermediate_df)
        

    return df



def retrieve_optimal_portfolio(ticker_df:pd.DataFrame, rat:int = None)->dict:
    """
    Given a risk assessment score, which is a measurement
    of a client's risk tolerance

    return a dictionary of investment vehicle with percentages that their 
    portfolio should allocate to each investment vehicle 
    """
    mean = expected_returns.mean_historical_return(ticker_df)

    sample_covar_mat = risk_models.sample_cov(ticker_df)

    ef = EfficientFrontier(mean,sample_covar_mat)

    print(f"the vars of ef are {vars(ef)}")

    pass





if __name__ == '__main__':
    tickers = scrape_stock_tickers()
    ticker_df = get_ticker_data(tickers)
    retrieve_optimal_portfolio(ticker_df)