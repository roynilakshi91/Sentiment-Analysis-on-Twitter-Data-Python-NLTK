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
q = 'the quent' 

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
from prettytable import PrettyTable
retweets = [
            
            (status['retweet_count'], 
             status['retweeted_status']['user']['screen_name'],
             status['text']) 
            
            
            for status in statuses 
            

                if status.has_key('retweeted_status')
           ]


pt = PrettyTable(field_names=['Count', 'Screen Name', 'Text'])
[ pt.add_row(row) for row in sorted(retweets, reverse=True)[:5] ]
pt.max_width['Text'] = 50
pt.align= 'l'
print pt
_retweets = twitter_api.statuses.retweets(id=317127304981667841)
print [r['user']['screen_name'] for r in _retweets]

