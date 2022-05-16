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
def handle_tickers_retrieve_data(tickers_list:list)->dict:
    """
    Given a list of tickers, retrieve data from yahoo finance

    returns a dictionary that will be saved as json
    """
    return_dict = dict()

    past_date = datetime.today() - timedelta(days=730)
    today = datetime.today()

    for ticker in tickers_list:

        ticker_obj = yf.Ticker(ticker)
        
        data: pd.Series = ticker_obj.history(start = past_date, end = today)['Close']
        data.rename(ticker, inplace=True)

        data.index = data.index.astype(str)

        #have to convert to a dictionary
        #because pd.Series are not json serializable
        cur_dict = {'dates' : list(data.index), 'ticker': list(data.values)}
        
        return_dict[ticker] = cur_dict

    return return_dict



def get_mutual_fund_data():
    """
    Read in excel files that have list of 
    each companies most popular/best performing mutual funds

    return data for each ticker
    """
    BASE_DIR = Path(__file__).resolve().parent.parent
    BASE_DIR = str(BASE_DIR)
    # BASE_DIR locally is /Users/stevebaca/PycharmProjects/TradePro_Reimagined/TradePro_Reimagined/scripts 

    mutual_fund_tickers_file_path = BASE_DIR + "/utils/static_list_of_tickers/mutual_fund_tickers.xlsx"
    mf_tickers_df = pd.read_excel(mutual_fund_tickers_file_path)

    vanguard_dict = handle_tickers_retrieve_data(mf_tickers_df['Vanguard_Ticker'].tolist())

    fidelity_dict = handle_tickers_retrieve_data(mf_tickers_df['Fidelity_Ticker'].tolist())

    schwab_dict = handle_tickers_retrieve_data(mf_tickers_df['Schwab_Ticker'].tolist())


    

    return vanguard_dict, fidelity_dict, schwab_dict



if __name__ == '__main__':
    get_mutual_fund_data()