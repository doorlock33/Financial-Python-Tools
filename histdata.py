import requests
import json
import pandas as pd 
import numpy as np 

import datetime as dt
from datetime import datetime
import csv

root_url = 'https://api.binance.com/api/v1/klines'

coin_c = input("Choose a coin: ")
pair = input("Choose a pair [Choose from: USDT, BTC, ETH]: ")

if pair == "USDT":
        coin = coin_c + pair
elif pair == "BTC":
        coin = coin_c + pair
elif pair == "ETH":
        coin = coin_c + pair

def get_bars(symbol, interval = '4h'):
    url = root_url + '?symbol=' + symbol + '&interval=' + interval
    data = json.loads(requests.get(url).text)
    df = pd.DataFrame(data)
    df.columns = ['open_time',
                 'o', 'h', 'l', 'c', 'v',
                 'close_time', 'qav', 'num_trades',
                 'taker_base_vol', 'taker_quote_vol', 'ignore']           
    df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.close_time]
    # df.reset_index(drop=True) This resets the index to the default integer index and removes the original one
    # df.reset_index(inplace=True)
    df.drop(["ignore"], axis=1, inplace=True)
    return df

coin = get_bars(f'{coin}')

# print(coin.to_string(index=False))

with open('C:/Users/User/Desktop/pyfund/finance/pricedata.txt', 'w', newline='\n') as d:
        # d.write(str(ncashbtc['open_time']))
        # d.write(str(ncashbtc['o']))
        # d.write(str(ncashbtc['c']))
        d.write(str(coin.to_string(index=False)))