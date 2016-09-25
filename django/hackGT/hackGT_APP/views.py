from django.http import HttpResponse
from django.shortcuts import render
import urllib2
import json
import oauth2
import os
import tweepy
import inspect
import sys
from training import machineLearning

print sys.stdout.encoding

CONSUMER_KEY = '6fqay2JAArGppgiVh5Kv8jUB9'
CONSUMER_SECRET = 'Hzuo4P3G5JBNFytAqvCPxcQomJ74VqIGAXOLrGjIla1GhbBk5A'
ACCESS_TOKEN = '779599701691760640-vHT54xE5aY21viNAYWpfqxvkrs89pUT'
ACCESS_SECRET = 'atZ8dx9C81wqh1Ht9TFXPaThYsyUoanlayXoNP0J0McCF'

stream_created = False
tweetList = []
test = False

def oauth_req(url, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=ACCESS_TOKEN, secret=ACCESS_SECRET)
    client = oauth2.Client(consumer, token)
    esp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

class MyStreamListener(tweepy.StreamListener):
    test = True
    n = 0
    def on_status(self, status):
        self.n = self.n + 1
        print self.n
        print status
        if 'coordinates' in status._json and status._json['coordinates'] != None:
            print status._json['coordinates']
        if status.coordinates:
            print status.coordinates
        #if 'coordinates' in status.author and status.author['coordinates'] != None:
        #    print status.author['coordinates']
        #if self.test:
            #print status
            #for property, value in vars(status).iteritems():
            #    print property, ": ", value
        self.test = False




def maps(request):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())

    myStream.filter(track=['Rihanna'], async=False)

    machineLearning.learn()
    indices = machineLearning.predict("PLACEHOLDER")

    return HttpResponse("testing")
