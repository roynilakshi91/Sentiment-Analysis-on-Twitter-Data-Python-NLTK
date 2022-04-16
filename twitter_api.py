import twitter
import json 
import psycopg2

api = twitter.Twitter(auth=twitter.OAuth('789506922−←􏰀 Q76Fuju6HXT5m4zkRd70TN4J4o9vTNnLUeXs1jDC ' , '←􏰀 UZAvAFrkD09QGJT9ZLrZ0B1kxi5bukHICKdpaxYDUzx5q ' , ' W94xcLqO4NhCrFKVSigwDk5yb ' , ' ←􏰀 U0LMMrj2eZOtxXr4zViYprO9nEuRJ8XEQt3iDD2vOqcKsIeZAW ' ) )

conn = psycopg2 . connect ( ” dbname=testdb user=postgres password=postgres ” ) 

cur = conn.cursor()

cur.execute('SELECT text from word') terms = cur.fetchall()

if terms :
    for t in terms:
        tweets = api.search.tweets(q=”t”, lang='en ' , count=100) 
        
        for s in tweets[ ' statuses ' ]:
            cur.execute(”SELECT * FROM tweet WHERE tid='%s '”, (s[ 'id '], ))
            # ignore the duplicate and RT−like tweets
            
            if cur.fetchone() is not None or s['text'].find('3g') >= 0:
                continue
            print s['id str']
            print s[ 'lang ']
            print s[ 'retweet count '] print s[ 'favorite count '] print s[ 'retweeted ']
            print s[ 'source ']
            print s[ 'user '][ 'location ']
            print s[ 'user '][ 'url ']
            print s[ 'features '][ 'type ']
            print s[ 'user '][ 'followers count '] 
            print s[ 'user '][ 'listed count '] 
            print s[ 'user '][ 'screen name '] 
            print s[ 'user '][ 'description '] 
            print s[ 'user '][ 'statuses count '] 
            print s[ 'user '][ 'following ']
            print s['in reply to user id'] 
            print s[ 'user '][ 'friends count '] 
            print s[ 'user '][ 'time zone ']
            print s['text']
            print s[ 'user '][ 'created at ']
            print s[ 'user '][ 'place id ']
            
            cur.execute( ” INSERT INTO tweet3 ( id_str , lang , retweet_count , favorite_count , ←􏰀 followers_count , listed_count , screen_name ,(%s,%s,%s,%s,%s,%s,%s)”, (s['idstr'],s['lang'],s['retweetcount'],s['←􏰀 favorite count'],s['retweeted'],s['source'],s['user']['location'],s['user']['
followercount' ],s['user'] ['listedcount'],s['user']['screenname'],s['user']['description'],s['user']['statuses count'],s['user']['following'],s['inreplytouserid'],s['user']['friendscount'],s['user']['timezone'],s['text'],s['createdat']))
               
             
            conn . commit ( )
            
            
cur. close () 
conn. close ()
                                                                                                                                                   

            
