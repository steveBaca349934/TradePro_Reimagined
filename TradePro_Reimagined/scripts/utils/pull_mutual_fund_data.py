import re
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, date
import sys
import copy
from datetime import datetime, timedelta
from pathlib import Path

# driver = webdriver.Chrome(chromedriver)
# driver.implicitly_wait(30)
def handle_tickers_retrieve_data(tickers_list:list, mutual_fund_company:str)->dict:
    """
    Given a list of tickers, retrieve data from yahoo finance

    returns a dictionary that will be saved as json
    """
    for ticker in tickers.get(financial_index):

        ticker_obj = yf.Ticker(ticker)
        
        data: pd.Series = ticker_obj.history(start = past_date, end = today)['Close']
        data.rename(ticker, inplace=True)



def get_mutual_fund_data():
    """
    Read in excel files that have list of 
    each companies most popular/best performing mutual funds

    return data for each ticker
    """
    BASE_DIR = Path(__file__).resolve().parent.parent
    BASE_DIR = str(BASE_DIR)
    # BASE_DIR locally is /Users/stevebaca/PycharmProjects/TradePro_Reimagined/TradePro_Reimagined/scripts 
    
    vanguard_file_path = BASE_DIR + "/utils/static_list_of_tickers/vanguard_tickers.xlsx"
    vanguard_tickers_df = pd.read_excel(vanguard_file_path)

    vanguard_dict = handle_tickers_retrieve_data(vanguard_tickers_df['Vanguard_Ticker'].tolist(), "Vanguard")
    # nasdaq_dict = dict()
    # djia_dict = dict()
    # for financial_index in tickers:
        
    #     index = 0
    #     for ticker in tickers.get(financial_index):

    #         ticker_obj = yf.Ticker(ticker)
            
    #         data: pd.Series = ticker_obj.history(start = past_date, end = today)['Close']
    #         data.rename(ticker, inplace=True)
            
    #         if financial_index == 'S_AND_P_500':
    #             s_and_p_500_dict[ticker] = data
    #         elif financial_index == 'NASDAQ':
    #             nasdaq_dict[ticker] = data
    #         else:
    #             djia_dict[ticker] = data

    # return s_and_p_500_dict, nasdaq_dict, djia_dict



if __name__ == '__main__':
    get_mutual_fund_data()