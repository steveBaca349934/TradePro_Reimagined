import re
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, date
import sys
import copy
from datetime import datetime, timedelta

def scrape_stock_tickers()->dict:
    """
    Uses pandas to get list of all stock tickers from S&P 500

    returns dict of stock tickers with keys as tickers, vals as full company name
    """
    
    res_dict = dict()

    # pulling S&P
    s_and_p_payload=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    s_and_p_stocks = s_and_p_payload[0]

    s_and_p_tickers = s_and_p_stocks['Symbol'].tolist()
    s_and_p_company_names = s_and_p_stocks['Security'].tolist()

    s_and_p_dict = dict()
    for index, ticker in enumerate(s_and_p_tickers):
        if ticker not in res_dict:
            res_dict[ticker] = s_and_p_company_names[index]

    # # pulling nasdaq
    # nasdaq_payload=pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')
    # nasdaq_stocks = nasdaq_payload[3]

    # nasdaq_tickers = nasdaq_stocks['Ticker'].tolist()
    # nasdaq_company_names = nasdaq_stocks['Company'].tolist()

    # for index, ticker in enumerate(nasdaq_tickers):
    #     if ticker not in res_dict:
    #         res_dict[ticker] = nasdaq_company_names[index]
    
    # # pulling djia
    # djia_payload=pd.read_html('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average')
    # djia_stocks = djia_payload[1]

    # djia_tickers = djia_stocks['Symbol'].tolist()
    # djia_company_names = djia_stocks['Company'].tolist()

    # for index, ticker in enumerate(djia_tickers):
    #     if ticker not in res_dict:
    #         res_dict[ticker] = djia_company_names[index]

    return res_dict

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

    index = 0
    for ticker in tickers:

        ticker_obj = yf.Ticker(ticker)
        
        data = ticker_obj.history(start = past_date, end = today)['Close']

        if len(data) != 0:

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

if __name__ == '__main__':

    tickers = scrape_stock_tickers()
    print(tickers)

    