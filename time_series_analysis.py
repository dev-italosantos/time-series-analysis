import pandas as pd
import matplotlib as plt
import yfinance as yt
import datetime

data_atual = datetime.datetime.now().date()

ticket = yt.Ticker('^BVSP')

df = ticket.history(interval='1d', start='2018-01-01', end=data_atual)

print(df.tail(2))

