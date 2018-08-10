import requests

def get_usd_rub_rate():
    '''Return the exchange rate from the open api'''

    url = 'http://free.currencyconverterapi.com/api/v5/convert?q=USD_RUB&compact=y'
    rate_dict = requests.get(url).json()
    rate = rate_dict['USD_RUB']['val']
    return rate
