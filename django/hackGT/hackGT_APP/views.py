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
import csv

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


def maps(request):
    f = open('data.csv', 'w')
    csvwriter = csv.writer(f)
    csvwriter.writerow(['Testing'])

    req = oauth_req('https://api.twitter.com/1.1/search/tweets.json?q=drugs&count=1&lang=en')
    data = json.loads(req)
    tweets = data['statuses']

    for tweet in tweets:
        csvwriter.writerow([tweet['text']])
    f.close()
    
    learner = machineLearning.machineLearning()
    indices = learner.predict("data.csv")
    return HttpResponse("testing")
