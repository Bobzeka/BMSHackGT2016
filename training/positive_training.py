import urllib2
import json
import csv


f = open('positive_training.csv', 'w')
wrt = csv.writer(f)

subreddits = [
        'https://www.reddit.com/r/opiates.json',
        'https://www.reddit.com/r/mdma.json',
        'https://www.reddit.com/r/cocaine.json'
]


for subreddit in subreddits:
    req = urllib2.urlopen('https://www.reddit.com/r/opiates.json').read()
    data = json.loads(req)
    data = data['data']['children']

    for post in data:
        if 'selftext' in post:
            text = [post['selftext'], '1']
        elif 'title' in post:
            text = [post['title'], '1']
        if text:
            wrt.writerows(text)







f.close()
