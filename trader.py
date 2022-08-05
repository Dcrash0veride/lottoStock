import pandas as pd
import pandas_datareader.data as pdr
import datetime

tickers = ['MSFT', 'NVDA', 'ETSY', 'FB', 'ATVI', 'UBER', 'BYND', 'AAPL', 'V', 'PBFX', 'AMRX']

close_prices = pd.DataFrame()
attempt = 0
drop = []
while len(tickers) != 0 and attempt <= 5:
    tickers = [j for j in tickers if j not in drop]
    for i in range(len(tickers)):
        try:
            temp = pdr.get_data_yahoo(tickers[i],datetime.date.today() - datetime.timedelta(3650), datetime.date.today())
            temp.dropna(inplace=True)
            close_prices[tickers[i]] - temp['Adj Close']
            drop.append(tickers[i])
        except:
            print(tickers[i], " :failed to fetch data...retrying")
            continue
    attempt += 1

close_prices.mean()
close_prices.median()
close_prices.std()
