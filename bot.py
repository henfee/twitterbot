import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from secrets import *
import json

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# COONSTANTS
WORDS = ["#Exxon", "#exxon", "ExxonMobil", "@exxonmobil", "#exxonmobil", "exxonmobil",
         "ExxonMobil"]


class StreamListener(tweepy.StreamListener):
    def on_connect(self):
        print("You are connected to the streaming API")

    def on_data(self, data):
        print(data.text)
        return True

    def on_error(self, status_code):
        print("An error has occured: " + repr(status_code))
        return False

listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)

