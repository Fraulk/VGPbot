import tweepy
import time
import datetime
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
    api.retweet(ids[n])
    print('Tweet retweeted at ', str(datetime.datetime.now()))

if __name__ == '__main__':
    while True:
        # The most used hashtag i think
        r = api.search(q = '#VGPUnite filter:media -filter:retweets -filter:videos', count = '35', include_entities = 'true')
        # print(r)
        id = []
        # file = open("log.txt", "w")
        for tweet in r:
            id.append(getId(tweet._json))
        #     entities = json.dumps(tweet._json['entities'], sort_keys=True, indent=4)
        #     entities = json.loads(entities)
        #     screen_name = json.dumps(tweet._json['user']['screen_name'], sort_keys=True, indent=4)
        #     file.write(json.dumps(tweet._json, sort_keys=True, indent=4))
        #     print(entities)
        #     if ('media' in entities):
        #         media = entities['media']
        #         file.write(json.dumps(media[0]['media_url'], sort_keys=True, indent=4))
        #         file.write(json.dumps(media, sort_keys=True, indent=4))
        #         print(screen_name)
        #         print(media[0]['media_url'])
        #     print(id)
        # file.close()

        # print(id)
        retweetRandmly(id)

        #Every hours
        time.sleep(3600)