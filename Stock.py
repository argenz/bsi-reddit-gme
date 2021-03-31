# https://towardsdatascience.com/free-stock-data-for-python-using-yahoo-finance-api-9dafd96cad2e
import yfinance as yf
# get info stock
GME = yf.Ticker("GME")

rawdata = GME.history(start="2020-03-20", end="2020-05-20", interval="1h" prepost= True)
print("hello data!")
