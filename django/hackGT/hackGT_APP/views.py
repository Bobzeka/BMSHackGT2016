from django.http import HttpResponse
from django.shortcuts import render
import urllib2
import json
import oauth2
import os
import tweepy
import inspect

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

stream_created = False

def oauth_req(url, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=ACCESS_TOKEN, secret=ACCESS_SECRET)
    client = oauth2.Client(consumer, token)
    esp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        for property, value in vars(status).iteritems():
            print property, ": ", value



def maps(request):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())

    myStream.filter(track=['drugs', 'twisted', 'dope'], async=True)

    return HttpResponse("testing")

