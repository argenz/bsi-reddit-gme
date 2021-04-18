from stock_functions import get_stockdata
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import regex as re
from collections import Counter

sub_df = pd.read_csv("/bsi-reddit-gme/pyfiles/sub_df.csv"")

# -- -- -- -- Plot number of Subs per day -- -- -- -- #

# makes dataframe with columns "created" and "count"
sub_df_date_count = (pd.to_datetime(sub_df['created'])
       .dt.floor('d')
       .value_counts()
       .rename_axis('created')
       .reset_index(name='count')
       .sort_values('created', ascending=False))
# plt.figure()
# plt.plot(sub_df_date_count['created'], sub_df_date_count["count"], "o-")

# -- -- -- -- Stock Data -- -- -- -- #

name = "GME"
start = "2020-12-20" 
end = "2021-02-19" 
interval = "1d"

stock_data = get_stockdata(name, start, end, interval)
#stock_data.to_csv("gme_stock_data.csv")

# -- Plot standardised price and sub count per day -- #

sub_std = sub_df_date_count.std(axis=0).iloc[1]
sub_df_date_count["z_count"] = sub_df_date_count["count"]/sub_std

stock_std = stock_data.std(axis=0).iloc[1]
stock_data["z_open"] = stock_data["Open"]/stock_std

# plt.figure()
# plt.plot(stock_data['Date'], stock_data["z_open"], "o-", label="Stock Price")
# plt.plot(sub_df_date_count["created"], sub_df_date_count["z_count"], "x-", label="Sub Count")
# plt.title("Standardised Price and Submission Count plotted daily")
# plt.xlabel('Day')
# plt.ylabel('z')
# plt.legend()
# plt.show()

# warning: only plotting open prices 
# TODO: standardise average between high and low of each day, and plot

# -- Title Analysis -- #

title_df = sub_df["title"].str.lower()
title_df = title_df.str.replace(r'[^\w\s]', '')  #replace any character that is not a word or a space with nothing
words = " ".join(title for title in title_df)
wd_freq_df = pd.DataFrame(Counter(words.split()), index=[1]).transpose().reset_index().rename(columns={"index": "word", 1: "frequency"}).sort_values(by=["frequency"], ascending=False)

# order per most frequent to least frequent 
# inspect the df, remove prepositions, articles, http addresses?... 


# WSB Lingo
lingo_df = pd.DataFrame({"lingo": ["diamond hand", "paper hand", "stonk", "tendie", "to the moon", "jpow", "yolo"]})
