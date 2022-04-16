import re
import sys
def processTweet ( tweet ) :
  
  tweet = tweet.lower()
  tweet = re.sub('((www\.[ˆ\s]+)|(https?://[ˆ\s]+))','URL',tweet) tweet = re.sub('@[ˆ\s]+','ATUSER',tweet)
  tweet = re.sub( '[\s]+ ' , ' ' , tweet)
  tweet = re.sub(r'#([ˆ\s]+) ' , r'\1 ' , tweet)
  tweet = tweet.strip('\'”') return tweet

fp = open( 'twitterdata.csv' , 'r ') 
line = fp.readline()

while line :
  processedTweet = processTweet(line)
  print processedTweet l
  ine = fp.readline()
  sys . stdout=open ( ” preprocessed . txt ” , ” a ” ) 
  
fp. close ()
