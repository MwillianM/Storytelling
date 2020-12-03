import tweepy
import json
import csv
import time

access_token = "example"
access_token_secret = "example"
consumer_key = "example"
consumer_secret = "example"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
tweets = []
search = '%23ViraViraCIRO OR %2317Neles OR %23EleNão OR %23FraudeNasUrnasEletrônicas OR %23FicaTemer -filter:retweets'
c = tweepy.Cursor(api.search, q=search,since='2018-10-07', tweet_mode='extended', until='2018-10-08', count=100, wait_on_rate_limit = True, wait_on_rate_limit_notify=True).items()
while True:
    try:
        t = c.next()._json
        tweets.append(t)
    except tweepy.TweepError:
        time.sleep(60)
        continue
    except StopIteration:
        break

with open('twitter.json','w') as f:
    f.write(json.dumps(tweets))
