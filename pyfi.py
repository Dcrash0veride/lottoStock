import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

yf.pdr_override()  # Activate yahoo finance workaround
now = dt.datetime.now()
stock = input("Enter the ticker symbol: ")

startyear = 2019
startmonth = 1
startday = 1
start = dt.datetime(startyear, startmonth, startday)

df = pdr.get_data_yahoo(stock, start, now)

ma = 50

smaString = "SMA_" + str(ma)

df[smaString] = df.iloc[:, 4].rolling(window=ma).mean()

df = df.iloc[ma:]

numH = 0

numC = 0

for i in df.index:
    if df["Adj Close"][i] > df[smaString][i]:
        print("Close is higher")
        numH+=1
    else:
        print("Close is lower")
        numC+=1

print(stock + " has closed higher " + str(numH) + " times")

print(stock + " has closed lower " + str(numC) + " times")
