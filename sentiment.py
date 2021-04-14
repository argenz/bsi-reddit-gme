import pandas as pd
from textblob import TextBlob, Word
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from lexicon import new_words, remove_emoji, space
from nltk.corpus import stopwords

from analysis import stock_data

# -- Sentiment Analysis -- # 

sub_df = pd.read_csv("sub_df.csv")
sent_df = sub_df[["created", "author", "title"]]

# --- Preprocessing 
sent_df["ptitle"] = sub_df["title"].str.lower().str.replace(r'[^\w\s]', '')
sent_df["ptitle"] = sent_df["ptitle"].apply(lambda x: remove_emoji(x))

#remove english stop words
stop = stopwords.words('english')
sent_df["ptitle"] = sent_df["ptitle"].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

#lemmatize -- Not working yet
#sent_df["ptitle"]= sent_df["ptitle"].apply(space)
# sent_df["ptitle"] = sent_df["ptitle"].apply(lambda x: " ".join(Word(x).lemmatize() for x in x.split()))   #lemmatize takes argument if word is not noun

# --- General Sentiment of Titles with TextBlob

sent_df["polarity_textBlob"] = sent_df["ptitle"].apply(lambda x: TextBlob(x).sentiment.polarity)
sent_df["created"] = pd.to_datetime(sent_df["created"]).dt.floor('d')

daily_sent_df_textBlob = sent_df[["created", "polarity_textBlob"]].groupby(["created"], as_index=False).mean()
daily_sent_df_textBlob["z_polarity_textBlob"] = daily_sent_df_textBlob["polarity_textBlob"]/daily_sent_df_textBlob["polarity_textBlob"].std(axis=0)

# --- Sentiment using Vader and styled lexicon

vader = SentimentIntensityAnalyzer()
vader.lexicon.update(new_words)

sent_df["polarity_vader"] = sent_df["ptitle"].apply(lambda x: vader.polarity_scores(x)["compound"])
# sent_df[sent_df["polarity_vader"]>= 0.8].to_csv("TopPolarityVader")
# sent_df[sent_df["polarity_vader"]<= 0.2].to_csv("BottomPolarityVader")

daily_sent_df_vader = sent_df[["created", "polarity_vader"]].groupby(["created"], as_index=False).mean()
daily_sent_df_vader["z_polarity_v"] = daily_sent_df_vader["polarity_vader"]/daily_sent_df_vader["polarity_vader"].std(axis=0)


# --- Plotting

plt.figure()
plt.plot(daily_sent_df_vader["created"], daily_sent_df_vader["z_polarity_v"], label="z_Polarity_vader")
plt.plot(daily_sent_df_textBlob["created"], daily_sent_df_textBlob["z_polarity_textBlob"], label="z_Polarity_textBlob")
plt.plot(stock_data['Date'], stock_data["z_open"], "o-", label="z_Stock_Price")
plt.xlabel("Day")
plt.ylabel("Polarity & Stock Price")
plt.legend()
plt.show()

# --- 

