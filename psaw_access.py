from psaw import PushshiftAPI
import datetime as dt
import logging as log

api = PushshiftAPI()
start_time =int(dt.datetime(2020, 12, 20).timestamp())   #(2020, 12, 20) --> (2021, 1, 20)
end_time = int(dt.datetime(2021,  2, 18).timestamp())     #(2021, 1, 20) --> (2021,  2, 1) --> (2021,  2, 18)

submissions = api.search_submissions(
                            after=start_time,
                            before=end_time,
                            subreddit='wallstreetbets',
                            filter=['url','author', 'title', 'subreddit'], 
                            #limit= 100
                            )
"""
def cycle_in_tf(end_year, end_month, end_day): 
    while y<=end_year:
        while m<=end_month:
            while d<=end_day: 
                print("ciao")
    return ""
      """  

mysubs = []
with open('wsb_all.txt', 'w') as f: 
    for sub in submissions: 
        wrds = sub.title.split()
        if "GME" not in wrds: continue 
        else: 
            mysubs.append(sub)
            log.warning(f"Sub title: {sub.title}")
            f.write(f"{sub}\n")

log.warning("End.")

