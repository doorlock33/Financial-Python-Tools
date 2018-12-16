import time
import datetime
from datetime import datetime as dt
import requests
import json
import threading
from clint.textui import colored

def picks():
   start_time = time.time()
   threading.Timer(10, picks).start()

   with open('C:/Users/User/Desktop/pyfund/finance/coins.txt', 'r') as file:
      topkek = (file.read())
      for coin in topkek.split():
         coins = coin + 'BTC'
         prices = requests.get(f'https://www.binance.com/api/v1/ticker/24hr?symbol={coins}').json()
         c_symbol = (prices['symbol'])
         c_prevcPrice = (prices['lastPrice'])
         c_priceChangeP = (prices['priceChangePercent'])
         print(colored.cyan('{:-^30}'.format(c_symbol)))
         print(colored.magenta('{: ^30}'.format(c_prevcPrice)))
         if c_priceChangeP[0].isdigit():
            print((colored.green('{: ^30}'.format(c_priceChangeP + " %"))))
         elif c_priceChangeP.startswith('-'):
            print((colored.red('{: ^30}'.format(c_priceChangeP + " %"))))


   print(colored.yellow('{:*^30}'.format(dt.now().strftime('%Y-%m-%d %H:%M:%S'))))
   print(time.time() - start_time, 's')
picks()