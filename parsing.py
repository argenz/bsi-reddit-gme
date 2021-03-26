import pandas as pd
import os 
import datetime as dt

# -- -- -- -- Parsing from CSV to pandas.DataFrame -- -- -- -- #
df_dict = {}
for filename in os.listdir("./files"):
    df_dict[filename] = pd.read_csv(f"./files/{filename}")

sub_df = pd.concat([df for df in df_dict.values()]).reset_index(drop=True)

#print(sub_df.head())
#print(sub_df.tail())

# convert utc to normal date
sub_df["created_utc"] = sub_df["created_utc"].apply(lambda x: dt.datetime.fromtimestamp(int(x)).strftime("%Y-%m-%d %H:%M:%S"))

#print(len(sub_df.index))
#print(sub_df.loc[478])
#print(sub_df.head())
#print(sub_df.tail())