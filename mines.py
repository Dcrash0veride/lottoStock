import os
import matplotlib.pyplot as plt
import pandas as pd
import bs4 as bs
import requests
import pickle
import datetime as dt
import yfinance as yf


def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text.strip()
        print(ticker)
        tickers.append(ticker)

    with open('sp500tickers.pickle', "wb") as f:
        pickle.dump(tickers, f)

    return tickers

def get_data_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", 'rb') as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    end_date = dt.datetime.now()

    start_date = dt.datetime.now() - dt.timedelta(30)

    cl_price = pd.DataFrame()

    for ticker in tickers:
        missed_connections = []
        print(ticker)
        try:
            if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
                cl_price[ticker] = yf.download(ticker, start_date, end_date)["Adj Close"]
                cl_price[ticker].to_csv('stock_dfs/{}.csv'.format(ticker))
            else:
                print('Already have {}'.format(ticker))
        except ValueError:
            missed_connections.append(ticker)

    if len(missed_connections) > 0:
        print("In case you care the following tickers could not be found:")
        print(missed_connections)


save_sp500_tickers()
get_data_yahoo()