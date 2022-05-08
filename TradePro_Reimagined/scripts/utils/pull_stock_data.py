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
        if ticker not in s_and_p_dict:
            s_and_p_dict[ticker] = s_and_p_company_names[index]

    res_dict['S_AND_P_500'] = s_and_p_dict

    # pulling nasdaq
    nasdaq_payload=pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')
    nasdaq_stocks = nasdaq_payload[3]

    nasdaq_tickers = nasdaq_stocks['Ticker'].tolist()
    nasdaq_company_names = nasdaq_stocks['Company'].tolist()

    nasdaq_dict = dict()

    for index, ticker in enumerate(nasdaq_tickers):
        if ticker not in nasdaq_dict:
            nasdaq_dict[ticker] = nasdaq_company_names[index]

    res_dict['NASDAQ'] = nasdaq_dict

    djia_dict = dict()

    # # pulling djia
    djia_payload=pd.read_html('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average')
    djia_stocks = djia_payload[1]

    djia_tickers = djia_stocks['Symbol'].tolist()
    djia_company_names = djia_stocks['Company'].tolist()

    for index, ticker in enumerate(djia_tickers):
        if ticker not in djia_dict:
            djia_dict[ticker] = djia_company_names[index]

    res_dict['DJIA'] = djia_dict

    return res_dict

def get_ticker_data(tickers:dict)->dict:
    """
    Given a list of stock market tickers

    Return a dataframe full of previous close data
    """
    past_date = datetime.today() - timedelta(days=730)
    today = datetime.today()

    s_and_p_500_dict = dict()
    nasdaq_dict = dict()
    djia_dict = dict()
    for financial_index in tickers:
       
        count = 0 
        for ticker in tickers.get(financial_index):

            ticker_obj = yf.Ticker(ticker)
            
            data: pd.Series = ticker_obj.history(start = past_date, end = today)['Close']
            data.rename(ticker, inplace=True)

            data.index = data.index.astype(str)

            #have to convert to a dictionary
            #because pd.Series are not json serializable
            cur_dict = {'dates' : list(data.index), 'ticker': list(data.values)}
           
            if financial_index == 'S_AND_P_500':
                s_and_p_500_dict[ticker] = cur_dict
            elif financial_index == 'NASDAQ':
                nasdaq_dict[ticker] = cur_dict
            else:
                djia_dict[ticker] = cur_dict

            count += 1

    return s_and_p_500_dict, nasdaq_dict, djia_dict

if __name__ == '__main__':

    tickers:dict = scrape_stock_tickers()
    get_ticker_data(tickers)

    