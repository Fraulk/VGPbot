import tweepy
import time as t
from datetime import datetime, time
import json
from random import randint
import requests

from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Get the recent tweets ids
def getId(tweet):
    id = json.dumps(tweet['id'])
    return id

# Randomly retweet latest tweets by picking the id
def retweetRandmly(tweets):
    n = randint(0, len(tweets) - 1)
    try:
        print(tweets[n])
        api.retweet(tweets[n])
        print('Tweet retweeted at', str(datetime.now()))
    except tweepy.error.TweepError as e:
        print("Already retweeted :", e)

# Need cleanup
def editBanner(searchResult):
    screenName = []
    mediaUrl = []
    for tweet in searchResult:
        entities = json.dumps(tweet._json['entities'], sort_keys=True, indent=4)
        entities = json.loads(entities)
        screen_name = json.dumps(tweet._json['user']['screen_name'], sort_keys=True, indent=4)
        screen_name = screen_name.replace('"', '')
        if ('media' in entities):
            media = entities['media']
            screenName.append(screen_name)
            mediaUrl.append(media[0]['media_url'])
    n = randint(0, len(screenName) - 1)
    print(mediaUrl[n], "by", screenName[n], "chosen as banner")
    img_data = requests.get(mediaUrl[n]).content
    with open('tmpbanner.jpg', 'wb') as handler:
        handler.write(img_data)
    api.update_profile_banner('tmpbanner.jpg')
    api.update_profile(description = 'A bot who retweet #VGPUnite tweets (the most used hashtag in the community so). Created by @freaksboi Still in beta. Banner by @' + screenName[n])

def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

if __name__ == '__main__':
    while True:
        # The most used hashtag i think
        r = api.search(q = '#VGPUnite filter:media -filter:retweets -filter:videos', count = '35', include_entities = 'true')
        # print(r)
        id = []
        for tweet in r:
            id.append(getId(tweet._json))
        
        # New banner from shots every day
        if(is_time_between(time(15, 00), time(16, 00))):
            editBanner(r)

        # print(id)
        retweetRandmly(id)

        #Every hours
        t.sleep(3600)