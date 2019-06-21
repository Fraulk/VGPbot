import tweepy
import time
import json
from random import randint

from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Get the recent tweets ids
def getId(tweet):
    id = json.dumps(tweet['id'])
    return id

#Randomly retweet latest tweets
def retweetRandmly(ids):
    n = randint(0, len(ids) - 1)
    print(ids[n])
    res = api.retweet(ids[n])
    print(res)

if __name__ == '__main__':
    while True:
        # The most used hashtag i think
        r = api.search('#VGPUnite')
        for tweet in r:
            id = [getId(tweet._json)]
            print(id)
        
        retweetRandmly(id)
        #Every hours
        time.sleep(3600)