from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from lexicon import new_words

from analysis import stock_data

# -- Sentiment Analysis -- # 

sub_df = pd.read_csv("sub_df.csv")

# --- General Sentiment of Titles with TextBlob
sent_df = sub_df[["created", "author", "title"]]
sent_df["polarity_textBlob"] = sent_df["title"].apply(lambda x: TextBlob(x).sentiment.polarity)
sent_df["created"] = pd.to_datetime(sent_df["created"]).dt.floor('d')

daily_sent_df_textBlob = sent_df[["created", "polarity_textBlob"]].groupby(["created"], as_index=False).mean()

# plt.figure()
# plt.plot(daily_sent_df_textBlob["created"], daily_sent_df_textBlob["polarity_textBlob"])
# plt.xlabel("Day")
# plt.ylabel("Polarity")
# plt.show()

# --- Sentiment using Vader and styled lexicon

vader = SentimentIntensityAnalyzer()
vader.lexicon.update(new_words)

sent_df["polarity_vader"] = sent_df["title"].apply(lambda x: vader.polarity_scores(x)["compound"])
sent_df[sent_df["polarity_vader"]>= 0.8].to_csv("TopPolarityVader")
sent_df[sent_df["polarity_vader"]<= 0.2].to_csv("BottomPolarityVader")



daily_sent_df_vader = sent_df[["created", "polarity_vader"]].groupby(["created"], as_index=False).mean()

daily_sent_df_vader["z_polarity_v"] = daily_sent_df_vader["polarity_vader"]/daily_sent_df_vader["polarity_vader"].std(axis=0)

# plt.figure()
# plt.plot(daily_sent_df_vader["created"], daily_sent_df_vader["z_polarity_v"], label="z_Polarity")
# plt.plot(stock_data['Date'], stock_data["z_open"], "o-", label="Stock Price")
# plt.xlabel("Day")
# plt.ylabel("Polarity & Stock Price")
# plt.legend()
# plt.show()

