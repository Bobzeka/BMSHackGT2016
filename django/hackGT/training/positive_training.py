import urllib2, base64
import json
import csv
import time


f = open('positive_training.csv', 'w')
wrt = csv.writer(f)

subreddits = [
        'https://www.reddit.com/r/opiates.json',
        'https://www.reddit.com/r/mdma.json',
        'https://www.reddit.com/r/cocaine.json'
]


for subreddit in subreddits:
    for n in range(0, 19):
        time.sleep(60)
        if n == 0:
            url = subreddit
        else:
            url = subreddit + '?after=' + after

        request = urllib2.Request(subreddit)
        auth = base64.b64encode('%s:%s' % ('bmshackgt', 'Hackin16'))
        request.add_header('Authorization', 'Basic %s' % auth)
        try:
            result = urllib2.urlopen(request)
        except:
            print subreddit
            print n
        result = result.read()
        data = json.loads(result)
        data = data['data']
        after = data['after']
        data = data['children']

        for post in data:
            post = post['data']
            text = ''
            if 'selftext' in post:
                text = [post['selftext'], '1']
            elif 'title' in post:
                text = [post['title'], '1']
            if text != '':
                wrt.writerows(text)


f.close()
