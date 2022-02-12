from django.shortcuts import render
import re
import yfinance as yf


def check_pw_is_robust(pw:str)->bool:
    """
    Checking if a password is of length 12, 
    Has two numbers in it, 
    And has a special character in it

    returns True or False
    """

    if len(pw) < 12:
        return False

    # check if there are at least two numbers in the string
    num_of_numbers = 0
    for char in pw:
        if char.isdigit():
            num_of_numbers += 1

    if num_of_numbers <= 1:
        return False

    # check if any special characters exist in the string
    special_characters = re.findall(r"[, .!?]", pw)
    if len(special_characters) < 1:
        return False


    return True


def send_email():
    pass



def scrape_web_data()->dict:

    # req = HistoricalPrices('AAPL', start_date = '2022-01-15', end_date = '2022-01-30')
    standard_poor_500 = yf.Ticker("^GSPC")
    standard_poor_500_prev_close = standard_poor_500.info.get('previousClose')

    ndaq = yf.Ticker("^IXIC")
    ndaq_prev_close = ndaq.info.get('previousClose')

    djia = yf.Ticker("^DJI")
    djia_prev_close = djia.info.get('previousClose')


    return {
        'S&P500': round(standard_poor_500_prev_close,1),
        'NASDAQ': round(ndaq_prev_close,1),
        'DJIA': round(djia_prev_close,1)
    }


def retrieve_optimal_portfolio(rat:int)->dict:
    """
    Given a risk assessment score, which is a measurement
    of a client's risk tolerance

    return a dictionary of investment vehicle with percentages that their 
    portfolio should allocate to each investment vehicle 
    """
    pass


if __name__ == '__main__':
    req = scrape_web_data()
    print(req)
    

