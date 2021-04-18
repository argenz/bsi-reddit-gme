from psaw import PushshiftAPI
import datetime as dt
import logging as log
import csv
import pandas as pd
import os 


# -- -- -- Methods for fetching Data from Pushshift API -- -- -- #

api = PushshiftAPI()
start_time = dt.datetime(2020, 12, 20) 
end_time = dt.datetime(2021,  2, 19)

# .TXT
# Accesses Pushshift API
# splits the time frame (%start_time and %end_time) in blocks of %time_delta days 
# Creates a separate .txt file for each block
# Each .txt files contains the Reddit submissions containing the word "GME" in the title
def throttle_requests_totxt(start_time, end_time, time_delta):
    tmp_etime = start_time + time_delta

    while tmp_etime < end_time:
        submissions = api.search_submissions(
                            after=int(start_time.timestamp()),
                            before=int(tmp_etime.timestamp()),
                            subreddit='wallstreetbets',
                            filter=['url', 'author', 'title',
                                'subreddit', 'created_utc'],
                            # limit= 100
                            )
        with open(f'wsb_{start_time}_{tmp_etime}.txt', 'w') as f:
            for sub in submissions:
                wrds = sub.title.split()
                if "GME" not in wrds: continue
                else:
                    log.warning(f"Sub title: {sub.title}")
                    f.write(f"{sub}\n")
            f.flush()

        start_time = tmp_etime
        tmp_etime = start_time + time_delta
    return "Done"

# # Uncomment Here below to download all .TXT files for the time period specifcied above
# x = throttle_requests_totxt(start_time, end_time, dt.timedelta(10)) #10 day cycle
# print(x)


# CSV 
# Accesses Pushshift API
# splits the time frame (%start_time and %end_time) in blocks of %time_delta days 
# Creates a separate .csv file for each block
# Each .csv files contains the Reddit submissions containing the word "GME" in the title
def throttle_requests_tocsv(start_time, end_time, time_delta):
    tmp_etime = start_time + time_delta

    while tmp_etime < end_time:
        submissions = api.search_submissions(
                            after=int(start_time.timestamp()),
                            before=int(tmp_etime.timestamp()),
                            subreddit='wallstreetbets',
                            filter=['url', 'author', 'title',
                                'subreddit', 'created_utc', 'id', 'score', 'upvote_ratio'],
                            # limit= 100
                            )

        with open(f'wsb_{start_time}_{tmp_etime}.csv', 'w') as f: 
            sub_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            sub_writer.writerow(['id', 'created_utc', 'author', 'title', 'url', 'score', 'upvote_ratio'])

            for sub in submissions: 
                wrds = sub.title.split()
                if "GME" not in wrds: continue 
                else: 
                    log.warning(f"Sub ID:{sub.id}, Sub created_utc: {sub.created_utc}, Sub title: {sub.title[:10]}, Sub score:{sub.score}")
                    sub_writer.writerow([sub.id, sub.created_utc, sub.author, sub.title, sub.url, sub.score, sub.upvote_ratio])           

        start_time = tmp_etime
        tmp_etime = start_time + time_delta
    return "Done"

# # Uncomment Here below to download all CSV files for the time period specifcied above
# x = throttle_requests_tocsv(start_time, end_time, dt.timedelta(10)) #10 day cycle
# print(x)
        
# -- -- -- -- Parsing from CSV to pandas.DataFrame -- -- -- -- #
df_dict = {}
for filename in os.listdir("./files"):
    df_dict[filename] = pd.read_csv(f"./files/{filename}")

sub_df = pd.concat([df for df in df_dict.values()]).reset_index(drop=True)

# convert utc to normal date
sub_df["created_utc"] = sub_df["created_utc"].apply(lambda x: dt.datetime.fromtimestamp(int(x)).strftime("%Y-%m-%d %H:%M:%S"))
sub_df.rename(columns={'created_utc':'created'}, inplace=True)

#sub_df.to_csv("sub_df_new.csv")
#print(sub_df.head())
#print(sub_df.tail())

