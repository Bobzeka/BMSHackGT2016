from django.http import HttpResponse
from django.shortcuts import render
import urllib2
import json
import oauth2
import os

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

def oauth_req(url, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=ACCESS_TOKEN, secret=ACCESS_SECRET)
    client = oauth2.Client(consumer, token)
    esp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content


def maps(request):
    req = oauth_req('https://api.twitter.com/1.1/account/verify_credentials.json')
    data = json.loads(req)

    print data

    return HttpResponse(req)

