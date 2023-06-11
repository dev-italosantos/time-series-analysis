import pandas as pd
import matplotlib as plt
import yfinance as yt

ticket = yt.Ticker('^BVSP')
df = ticket.history(period = '5y', interval = '1d')

print(df)
