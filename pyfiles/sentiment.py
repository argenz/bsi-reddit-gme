import pandas as pd
from textblob import TextBlob, Word
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from lexicon import new_words, new_words_updated, remove_emoji, space, update_new_words
from nltk.corpus import stopwords

from analysis import stock_data
# -- Sentiment Analysis -- # 

sub_df = pd.read_csv("/Users/FCRA/Desktop/ALL/BSI/bsi-reddit-gme/pyfiles/sub_df.csv")
sent_df = sub_df[["created", "author", "title"]]

# already preproc titles
sub_df2 = pd.read_csv("/Users/FCRA/Desktop/ALL/BSI/bsi-reddit-gme/sentiment_files/preproc_titles.csv").reset_index(drop=True)
sent_df["ptitle"] = sub_df2["title"]

# --- General Sentiment of Titles with TextBlob

sent_df["polarity_textBlob"] = sent_df["ptitle"].apply(lambda x: TextBlob(x).sentiment.polarity)
sent_df["created"] = pd.to_datetime(sent_df["created"]).dt.floor('d')

daily_sent_df_textBlob = sent_df[["created", "polarity_textBlob"]].groupby(["created"], as_index=False).mean()
daily_sent_df_textBlob["z_polarity_textBlob"] = daily_sent_df_textBlob["polarity_textBlob"]/daily_sent_df_textBlob["polarity_textBlob"].std(axis=0)

#sent_df[["ptitle", "polarity_textBlob"]].to_csv("titles_textblob.csv")

# --- Sentiment using Vader and styled lexicon

vader = SentimentIntensityAnalyzer()
vader.lexicon.update(new_words)

sent_df["polarity_vader"] = sent_df["ptitle"].apply(lambda x: vader.polarity_scores(x)["compound"])
# sent_df[sent_df["polarity_vader"]>= 0.8].to_csv("TopPolarityVader")
# sent_df[sent_df["polarity_vader"]<= 0.2].to_csv("BottomPolarityVader")

daily_sent_df_vader = sent_df[["created", "polarity_vader"]].groupby(["created"], as_index=False).mean()
daily_sent_df_vader["z_polarity_v"] = daily_sent_df_vader["polarity_vader"]/daily_sent_df_vader["polarity_vader"].std(axis=0)

# # --- New Words
df_most_freq = pd.read_csv("/Users/FCRA/Desktop/ALL/BSI/bsi-reddit-gme/Notebooks/frequent_words.csv")
incoming_words = df_most_freq["word"].tolist()
new_word_set = update_new_words(new_words, incoming_words)

vader.lexicon.update(new_words_updated)

sent_df["polarity_vader_up"] = sent_df["ptitle"].apply(lambda x: vader.polarity_scores(x)["compound"])
daily_sent_df_vader_up = sent_df[["created", "polarity_vader_up"]].groupby(["created"], as_index=False).mean()
daily_sent_df_vader_up["z_polarity_vup"] = daily_sent_df_vader_up["polarity_vader_up"]/daily_sent_df_vader_up["polarity_vader_up"].std(axis=0)

# # --- Plotting

plt.figure()
plt.plot(daily_sent_df_vader["created"], daily_sent_df_vader["z_polarity_v"], label="z_Polarity_vader")
plt.plot(daily_sent_df_vader["created"], daily_sent_df_vader_up["z_polarity_vup"], label="z_Polarity_vader_update")
plt.plot(daily_sent_df_textBlob["created"], daily_sent_df_textBlob["z_polarity_textBlob"], label="z_Polarity_textBlob")
plt.plot(stock_data['Date'], stock_data["z_open"], "o-", label="z_Stock_Price")
plt.xlabel("Day")
plt.ylabel("Polarity & Stock Price")
plt.legend()
plt.show()


