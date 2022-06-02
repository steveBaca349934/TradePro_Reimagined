from Historic_Crypto import Cryptocurrencies, HistoricalData
from datetime import datetime, date
import sys
import copy
from datetime import datetime, timedelta

SECONDS_IN_A_DAY = 86400

def get_crypto_data(list_of_crypto_pairs:list)->dict:
    """
    Given a list of crypto pairs that The webapp needs data 
    for. Pull historic data utilizing Historic_Crypto

    returns a dict which will be saved as json
    """
    return_dict = dict()

    past_date = datetime.today() - timedelta(days=1278)

    # YYYY-MM-DD-HH-MM 
    past_date_correct_format = past_date.strftime("%Y-%m-%d-%H-%M")

    for crypto_pair in list_of_crypto_pairs:

        cur_data = HistoricalData(crypto_pair,SECONDS_IN_A_DAY,past_date_correct_format).retrieve_data()
        
        cleaned_crypto_df = cur_data.reset_index()[['time','close']]

        cleaned_crypto_df['time'] = cleaned_crypto_df['time'].astype(str)

        #have to convert to a dictionary
        #so the data will be serializable
        cur_dict = {'dates' : list(cleaned_crypto_df['time'])
                   ,'ticker': list(cleaned_crypto_df['close'])}

        crypto_ticker = crypto_pair.split("-")[0]

        return_dict[crypto_ticker] = cur_dict


    return return_dict


def get_list_of_crypto_pairs()->list:
    """
    Utilize the "Historic_Crypto" library to pull 
    a list of Crypto 'pairs'.
    
    returns list of crypto pairs
    """
    crypto_pairs_df = Cryptocurrencies().find_crypto_pairs()

    # only pulling pairs that are USD
    return [pair for pair in crypto_pairs_df['id'] if pair.split("-")[1] == 'USD']

      
if __name__ == '__main__':
    crypto_pairs_list = get_list_of_crypto_pairs()
    get_crypto_data(crypto_pairs_list)
