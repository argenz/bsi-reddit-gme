from psaw import PushshiftAPI
import datetime as dt
import logging as log

api = PushshiftAPI()
start_time =dt.datetime(2020, 12, 20)   #(2020, 12, 20) --> (2021, 1, 20)
end_time = dt.datetime(2021,  2, 18)     #(2021, 1, 20) --> (2021,  2, 1) --> (2021,  2, 18)

""" submissions = api.search_submissions(
                            after=int(start_time.timestamp()),
                            before=int(end_time.timestamp()),
                            subreddit='wallstreetbets',
                            filter=['url','author', 'title', 'subreddit'], 
                            #limit= 100
                            ) """


def throttle_requests(start_time, end_time, time_delta): 
    tmp_etime = start_time + time_delta

    while tmp_etime<end_time: 
        submissions = api.search_submissions(
                            after=int(start_time.timestamp()),
                            before=int(tmp_etime.timestamp()),
                            subreddit='wallstreetbets',
                            filter=['url','author', 'title', 'subreddit'], 
                            #limit= 100
                            )
        #mysubs = []
        with open(f'wsb_{start_time}_{tmp_etime}.txt', 'w') as f: 
            for sub in submissions: 
                wrds = sub.title.split()
                if "GME" not in wrds: continue 
                else: 
                    #mysubs.append(sub)
                    log.warning(f"Sub title: {sub.title}")
                    f.write(f"{sub}\n")
            f.flush()            

        start_time = tmp_etime
        tmp_etime = start_time + time_delta
    return "Done"

x = throttle_requests(start_time, end_time, dt.timedelta(10)) #10 day cycle
print(x)

""" print(dt.timedelta(10))
print(start_time)
print(start_time + dt.timedelta(10))
print(end_time>end_time) """



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

"""

#TODO: Reddit
# - PREPPING: convert to csv, clean and parse data, change the time in human format #Francesca 
# - 
# - PLOTTING: 
# - - weekly frequnecy 
# - - monthly frequency 
# 
# - Deeper analysis on the Titles. "Hold", "to the Moon", WSB Lingo. NLTK? 
# - Deeper analysis on Authors. Most active (frequency of submissions), who receives the most likes/ups (quality). 
# 
# - Extras:
# - Look at twitter
# - ML

#TODO: GME Stock #Marco
# - download the stock data, datareader  
# - look at market (bull/bear, rational/irrational investors)
# RESEARCH:
# - Influence of others events (Stops, news, restrictions on trading platforms (e.g. robinhood)) 
# check pre-market, compare with reddit activity 
#
#TODO: correlation 
# - find correlation 
# - draw conclusions 