""" 
with open('wsb_all.txt', 'w') as f:
    for sub in mysubs:
        f.write(f"{sub}\n")



reddit = praw.Reddit(client_id = "F0aNrK4FulYznA",
                    client_secret = "52jkFYII-WXYfE7znhrOAcsAkfhvIg",
                    user_agent="redgmev1")

wsb = reddit.subreddit("wallstreetbets")

# period 01-01-2021 -> 01-02-2021
# gme_wsb = wsb.search("GME", month="01-01-2021")
# subm_gme = wsb.submissions(start=1609455600, end=1612134000, extra_query="gme")
# appareandlt the method submissions was deprecated in 2018 and reddit API does not allow for searching in a specific time frame 
# so I found that you can use pushift.io

import requests

headers = {
    'authority': 'api.pushshift.io',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.reddit.com/',
    'accept-language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7',
    'cookie': '__cfduid=d8aa4c96d0195b6408b74f45c281428731616012617',
}

params = (
    ('subreddit', 'wallstreetbets'),
    ('after', '1609484400'),
    ('before', '1612162800'),
)

response = requests.get('https://api.pushshift.io/reddit/submission/search/', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://api.pushshift.io/reddit/submission/search/?subreddit=news&after=2018-07-01&before=2018-08-01', headers=headers)

print(response.text) """