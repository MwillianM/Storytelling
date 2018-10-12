import tweepy
import json
import csv
import time
'''
access_token = "1045030220330397696-EkwpeLpmvtVaC4iCs4r2PUs5tPqPuH"
access_token_secret = "v0ScjA2RfGZnupEBwdhXYWqkIBu8lLB6Y60LnJj5gElpL"
consumer_key = "xlPOZAuQoeVDsXzoBck3b0tzp"
consumer_secret = "cDGnkfJRsZgq60Emp3OYEcle6LldwRqHtXzmj7sZqeZQovvKZi"
'''
access_token = "1045030220330397696-8CEACVDpQqVzwdnG8zpKSbGeeGnzXE"
access_token_secret = "0NEOIIu4nWlPd2zgrcmnKO2CGjcuUM1p4hwBeKzHIV9Bs"
consumer_key = "3TfPrLsXtI4UDy46vC3IMmFj8"
consumer_secret = "4bQoC405SBbNfriw784WooY7ZkuE77di18LF2StyXUI07Goqmv"

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