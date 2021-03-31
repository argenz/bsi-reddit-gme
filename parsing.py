import pandas as pd
import os 
import datetime as dt
import matplotlib.pyplot as plt

# -- -- -- -- Parsing from CSV to pandas.DataFrame -- -- -- -- #
df_dict = {}
for filename in os.listdir("./files"):
    df_dict[filename] = pd.read_csv(f"./files/{filename}")

sub_df = pd.concat([df for df in df_dict.values()]).reset_index(drop=True)

# convert utc to normal date
sub_df["created_utc"] = sub_df["created_utc"].apply(lambda x: dt.datetime.fromtimestamp(int(x)).strftime("%Y-%m-%d %H:%M:%S"))
sub_df.rename(columns={'created_utc':'created'}, inplace=True)

sub_df.to_csv("sub_df.csv")
#print(sub_df.head())
#print(sub_df.tail())

# -- -- -- -- Plot number of Subs per day -- -- -- -- #

sub_df_date_count = (pd.to_datetime(sub_df['created'])
       .dt.floor('d')
       .value_counts()
       .rename_axis('created')
       .reset_index(name='count')
       .sort_values('created', ascending=False))

#print(sub_df_date_count)

plt.plot(sub_df_date_count['created'], sub_df_date_count["count"], "o-")
plt.show()

# look at number of active members 
# look at % increase/decrease, diminishing returns from additional users in stock price. 
# (readers (buyers) != writers) 
# still holding, look at % of posts that wrote "still holding" to see what the activity was about. 

