import json

<<<<<<< HEAD
from API.models import StockData, MutualFundData, BenchMarkStockData
=======
from API.models import StockData, MutualFundData
>>>>>>> origin/master
from scripts.utils import pull_mutual_fund_data as pmfd
from scripts.utils import pull_stock_data as psd
from scripts.utils import pull_benchmark_s_and_p_data as pbm

"""
Job to populate DB with Stock and Mutual Fund Daily Data.
Should be run on a daily schedule 

in order to update cronjob need to do "python3 manage.py crontab add"
in order to do a test run need to do "python3 manage.py crontab run <some_hash>" (the hash will have appeared in the previous step)
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

    s_and_p_benchmark_dict = pbm.get_benchmark_data()

    BenchMarkStockData.objects.all().delete()

    update_bench_mark_stock_data = BenchMarkStockData.objects.create(
                                    s_and_p_500_benchmark  = json.dumps(s_and_p_benchmark_dict)
                                )

    update_bench_mark_stock_data.save()


    print("\n \n \n complete complete complete ! The world is saved \n ")

if __name__ == '__main__':
    run()