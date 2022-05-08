from django.shortcuts import render
from selenium import webdriver
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
from pandas_datareader import data

driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(30)


def scrape_stock_tickers()->dict:
    """
    Uses pandas to get list of all stock tickers from S&P 500

    returns dict of stock tickers with keys as tickers, vals as full company name
    """
    
    res_dict = dict()

    driver.get('https://investor.vanguard.com/investment-products/list/mutual-funds')
    df=pd.read_html(driver.find_element_by_id("history_table").get_attribute('outerHTML'))[0]

    vanguard_payload=pd.read_html('https://investor.vanguard.com/investment-products/list/mutual-funds')
    print(vanguard_payload)
    # s_and_p_stocks = s_and_p_payload[0]

    # s_and_p_tickers = s_and_p_stocks['Symbol'].tolist()
    # s_and_p_company_names = s_and_p_stocks['Security'].tolist()

    # for index, ticker in enumerate(s_and_p_tickers):
    #     if ticker not in res_dict:
    #         res_dict[ticker] = s_and_p_company_names[index]
    

    # return res_dict

if __name__ == '__main__':

    print(scrape_stock_tickers())
