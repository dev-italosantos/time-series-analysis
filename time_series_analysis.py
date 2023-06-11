import pandas as pd
import matplotlib as plt
import yfinance as yt
import datetime

data_atual = datetime.datetime.now().date()
start_date = '2018-01-01'

ticket = yt.Ticker('^BVSP')

df = ticket.history(interval='1d', start=start_date, end=data_atual)

print(df[['Close']])
print(df.tail(2))