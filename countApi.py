import twitter
import json
from prettytable import PrettyTable

CONSUMER_KEY = 'RYWdEZa4yHZfo0X4yuWKgUH7Z'
CONSUMER_SECRET = 'eXjJpxohvh9odH94kFZkyzxRuHlLfiJmJYZIPvXbycGHZMjyHR'
OAUTH_TOKEN = '789506922-NV4iivdNCsTyeqRcTyzpzXT1XuZpjAp2YvcPBkqU'
OAUTH_TOKEN_SECRET = 'Wmjo55K7PG5uROEK14iegaEj88SD2uBldWigZFTZ69s5n'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)
print twitter_api
WORLD_WOE_ID = 1
US_WOE_ID = 23424977



world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

print world_trends
print
print us_trends
import json

print json.dumps(world_trends, indent=1)
print
print json.dumps(us_trends, indent=1)
q = 'OMG facts' 

count = 100



search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']




for _ in range(5):
    print "Length of statuses", len(statuses)
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError, e: 
        break
   
    kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
    
    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']


print json.dumps(statuses[0], indent=1)
status_texts = [ status['text'] 
                 for status in statuses ]

screen_names = [ user_mention['screen_name'] 
                 for status in statuses
                     for user_mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text'] 
             for status in statuses
                 for hashtag in status['entities']['hashtags'] ]


words = [ w 
          for t in status_texts 
              for w in t.split() ]



print json.dumps(status_texts[0:5], indent=1)
print json.dumps(screen_names[0:5], indent=1) 
print json.dumps(hashtags[0:5], indent=1)
print json.dumps(words[0:5], indent=1)
from collections import Counter

for item in [words, screen_names, hashtags]:
    c = Counter(item)
    print c.most_common()[:10] 
    print
    from prettytable import PrettyTable

for label, data in (('Word', words), 
                    ('Screen Name', screen_names), 
                    ('Hashtag', hashtags)):
    pt = PrettyTable(field_names=[label, 'Count']) 
    c = Counter(data)
    [ pt.add_row(kv) for kv in c.most_common()[:10] ]
    pt.align[label], pt.align['Count'] = 'l', 'r' 
    print pt
