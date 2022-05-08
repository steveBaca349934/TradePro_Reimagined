import json
from django.conf import settings
from django.core.cache import caches

from API.models import StockData, MutualFundData

from scripts.utils import database_writer as dw
from scripts.utils import pull_mutual_fund_data as pmfd
from scripts.utils import pull_stock_data as psd

"""
Job to populate DB with Stock and Mutual Fund Daily Data.
Should be run on a daily schedule 

in order to run this script need to do "python3 manage.py runscript main"
"""

def run():

    res_dict = psd.scrape_stock_tickers()
    s_and_p_500_dict, nasdaq_dict, djia_dict = psd.get_ticker_data(res_dict)
    StockData.objects.all().delete()

  

    update_stock_data = StockData.objects.create(s_and_p_500=json.dumps(s_and_p_500_dict),
                                                         nasdaq=json.dumps(nasdaq_dict), djia = json.dumps(djia_dict))

    update_stock_data.save()

    vanguard_dict, fidelity_dict, schwab_dict = pmfd.get_mutual_fund_data()

    MutualFundData.objects.all().delete()

    update_mutual_fund_data = MutualFundData.objects.create(vanguard=json.dumps(vanguard_dict),
                                fidelity=json.dumps(fidelity_dict),schwab=json.dumps(schwab_dict))

    update_mutual_fund_data.save()

    print("\n \n \n complete complete complete ! The world is saved \n ")
   


if __name__ == '__main__':
    run()