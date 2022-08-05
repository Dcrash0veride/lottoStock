import datetime
import yfinance as yf
import pandas as pd

watch_list = ["AMZN", "LORL", "PBFX", "AMD", "TSLA", "GRUB", "SPY", "MSFT"]

end_date = datetime.datetime.now()

start_date = datetime.datetime.now() - datetime.timedelta(30)

cl_price = pd.DataFrame()

ohlcv_data = {}

data = yf.download("msft", period="6mo")

diff_data = yf.download("msft", period="1mo", interval="5m")



for ticker in watch_list:
    cl_price[ticker] = yf.download(ticker, start_date, end_date)["Adj Close"]

for ticker in watch_list:
    ohlcv_data[ticker] = yf.download(ticker, start_date, end_date,)["Adj Close"]

print(ohlcv_data)