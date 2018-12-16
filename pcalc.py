import requests
import json
from decimal import Decimal
from clint.textui import colored

exchange = input("Choose exchange: ")

if exchange == 'binance':
    ticker = input("Choose ticker: ").upper()
elif exchange == 'okex':
    ticker = input("Choose ticker: ").lower()
b_at = input("Bought at: ")

# file = open('C:/Users/User/Desktop/stuff/b_data.txt', 'w')

# with open('C:/Users/User/Desktop/stuff/b_data.txt', 'a+') as file:
#     openfile.append(b_at)

with open("C:/Users/User/Desktop/pyfund/finance/bdata/b_data.txt", "a") as file:
    file.write(b_at + " " + ticker + "\n")


if exchange == 'binance':
    price_binance = requests.get(f'https://www.binance.com/api/v3/ticker/price?symbol={ticker}' + 'BTC').json()
elif exchange == 'okex':
    price_okex = requests.get(f'https://www.okex.com/api/v1/ticker.do?symbol={ticker}' + '_btc').json()

b_at_l = []
b_at_l.append(b_at)

result_b = [Decimal(x.strip(' ')) for x in b_at_l]

if exchange == 'binance':
    cprice = (price_binance['price'])
elif exchange == 'okex':
    cprice = (price_okex['ticker']['last'])

# print(cprice)

plist = []
plist.append(cprice)

result = [Decimal(x.strip(' ')) for x in plist]

print(result[0] - result_b[0])

prices = []

prices.append(result)
prices.append(result_b)

# for result, result_b in zip(prices[::1], prices[1::1]):
#     print(100 * (result[0] - result_b[0]) / result[0])

def get_change(current, result_b):
    if result == result_b:
        return 100
    try:
        return (abs(result[0] - result_b[0]) / result_b[0]) * 100
    except ZeroDivisionError:
        return 0

print("Profit/loss: " + (colored.green("{0:.3}".format(get_change(result, result_b)) + " %")))