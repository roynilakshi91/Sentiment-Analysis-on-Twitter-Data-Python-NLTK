from twython import Twython
import csv

TWITTER_APP_KEY = 'RYWdEZa4yHZfo0X4yuWKgUH7Z'
TWITTER_APP_KEY_SECRET = 'eXjJpxohvh9odH94kFZkyzxRuHlLfiJmJYZIPvXbycGHZMjyHR'
TWITTER_ACCESS_TOKEN = '789506922-NV4iivdNCsTyeqRcTyzpzXT1XuZpjAp2YvcPBkqU'
TWITTER_ACCESS_TOKEN_SECRET = 'Wmjo55K7PG5uROEK14iegaEj88SD2uBldWigZFTZ69s5n'

t = Twython(app_key = TWITTER_APP_KEY, app_secret = TWITTER_APP_KEY_SECRET, oauth_token = TWITTER_ACCESS_TOKEN, oauth_token_secret = TWITTER_ACCESS_TOKEN_SECRET)

places = [place.lower() for place in open('place.txt', 'r').read().split(',')]

def search(query, count=100000000):
        print '\n\n----------------------------------------'
        search = t.search(q=query ,count=count)
        tweets = search['statuses']
        print 'Showing results for ', query
        out = []
        for tweet in tweets:
                has_place = False
                for place in places:
                        if place in tweet['text'].lower():
                                has_place = True
                                break

                
                
                #print tweet, "\n"
                #print tweet['id_str'], '\n', tweet['text'], '\n\n\n'
                if has_place:
                       out.append(['tagged', tweet['id_str'], query, tweet['geo'], tweet['text'].encode('ascii', 'ignore')])
                else:
                        out.append(['', tweet['id_str'], query, tweet['geo'], tweet['text'].encode('ascii', 'ignore')])
        return out

out = []
for word in open('brand.txt').read().split(','):
        out.extend(search(word.lower()))
                
with open('datacollection.csv', 'w') as f:
        writer = csv.writer(f)
        for row in out:
                writer.writerow(row)
