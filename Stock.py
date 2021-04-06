# https://towardsdatascience.com/free-stock-data-for-python-using-yahoo-finance-api-9dafd96cad2e
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

# get info stock
GME = yf.Ticker("GME")

rawdata = GME.history(start="2020-03-20", end="2020-05-20", interval="1h", prepost= True)
print(rawdata)
print("hello!")

# graph data
plt.plot(rawdata.index, rawdata["Close"],)
print(rawdata.index)
print(rawdata.columns)
plt.show()

#new column with time data
rawdata.index
time = rawdata.index
rawdata['time'] = time

