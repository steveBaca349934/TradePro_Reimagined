import re
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, date
import sys
import copy
from datetime import datetime, timedelta

def get_benchmark_data():

    standard_poor_500_ticker_obj = yf.Ticker("^GSPC")

    past_date = datetime.today() - timedelta(days=1278)
    today = datetime.today()

    s_and_p_500_dict = dict()

    data_series = standard_poor_500_ticker_obj.history(start = past_date, end = today)['Close']

    data_series.rename("s_and_p", inplace=True)
    data_series.index = data_series.index.astype(str)

    cur_dict = {'dates' : list(data_series.index), 'ticker': list(data_series.values)}

    return cur_dict

if __name__ == '__main__':
    print(get_benchmark_data())




