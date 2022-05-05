from django.conf import settings
from django.core.cache import caches

from utils import database_writer as dw
from utils import pull_mutual_fund_data as pmfd
from utils import pull_stock_data as psd



"""
Job to populate DB with Stock and Mutual Fund Daily Data.
Should be run on a daily schedule (as the DailyJob indicates lol)
"""

def run():

    res_dict = psd.scrape_stock_tickers(True,True,True)
    res_df = psd.get_ticker_data(res_dict)

    print("\n \n \n complete complete complete ! The world is saved \n ")


if __name__ == '__main__':
    run()