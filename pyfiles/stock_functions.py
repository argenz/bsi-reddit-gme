# https://towardsdatascience.com/free-stock-data-for-python-using-yahoo-finance-api-9dafd96cad2e
import yfinance as yf

# name = "GME"
# start = "2020-03-20"
# end = "2020-05-20"
# interval = "1h"

# get info stock
def get_stockdata(name, start, end, interval):
    GME = yf.Ticker(name)
    stock_data = GME.history(start=start, end=end, interval=interval, prepost= True)
    stock_data.reset_index(inplace=True)
    return stock_data

