import re
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, date
import sys
import copy
from datetime import datetime, timedelta
from pathlib import Path
from typing import List

# For getting and parsing the data from the website
from bs4 import BeautifulSoup
import requests
import re

# driver = webdriver.Chrome(chromedriver)
# driver.implicitly_wait(30)
def handle_tickers_retrieve_data(tickers_list:list)->dict:
    """
    Given a list of tickers, retrieve data from yahoo finance

    returns a dictionary that will be saved as json
    """
    return_dict = dict()

    past_date = datetime.today() - timedelta(days=1278)
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
    ** Decided to just hardcode in the tickers **

    return data for each ticker
    """
    vanguard_dict = handle_tickers_retrieve_data(
       [ 'VTAPX', 
        'VGPMX',
        'VHCIX',
        'VITAX',
        'VIPSX',
        'VMCTX',
        'VRGWX',
        'VMGAX',
        'VMSXX',
        'VINIX']
    )

    fidelity_dict = handle_tickers_retrieve_data(
        ['FDCPX'
        ,'FSIPX'
        ,'FYHTX'
        ,'FSHCX'
        ,'FACVX'
        ,'FWATX'
        ,'FITLX'
        ,'FFIDX'
        ,'FLCEX'
        ,'FLGEX']
    )

    schwab_dict = handle_tickers_retrieve_data(
        scrape_schwab_mf_tickers() + scrape_schwab_etf_tickers()
    )


    

    return vanguard_dict, fidelity_dict, schwab_dict


def scrape_schwab_etf_tickers() -> List[str]:
    """
    scrape schwab ETF and MF tickers
    off the world wide web
    
    return list of tickers
    """
    link = 'https://etfdb.com/etfs/issuers/charles-schwab/'

    # Grab data from website
    page_response = requests.get(link, timeout=1000)

    # Structure the raw data so that we can parse it
    soup = BeautifulSoup(page_response.content, features="lxml")

    
    etf_table = soup.find("table", {"id": "etfs"})

    rows = [] 
    # SCRAPE: Extract Table Contents
    for row in etf_table.tbody.findAll('tr'):
        rows.append ([col.text for col in row.findAll('td')])  # Gather all columns in the row

    ticker_list = [row[0] for row in rows]

    return ticker_list


def scrape_schwab_mf_tickers() -> List[str]:
    """
    scrape schwab ETF and MF tickers
    off the world wide web
    
    return list of tickers
    """
    link = 'https://mutualfunds.com/fund-company/charles-schwab-funds/'

    # Grab data from website
    page_response = requests.get(link, timeout=1000)

    # Structure the raw data so that we can parse it
    soup = BeautifulSoup(page_response.content, features="lxml")

    
    # mf_divs = soup.find("div", {"class": "mp-table-body-row-container"})

    ticker_list = []
    mf_p = soup.findAll("p", {"class": "m-table-body-subtext"})
    for row in mf_p:
        if row.span is not None:
            ticker_list.append(row.span.getText())
    

    
    return ticker_list




if __name__ == '__main__':
    print(scrape_schwab_mf_tickers())
    # get_mutual_fund_data()