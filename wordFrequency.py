def countWordFrequency(Data1):
   myDict = {}
   fh = open(Data1, 'r')
   content = fh.read()
   listWords = content.split(" ")
   for w in listWords:
      if (myDict.has_key(w)):
         myDict[w] = myDict[w] + 1
      else:
         myDict[w] = 1
   fh.close()
   return myDict

freq = countWordFrequency('tweet_sentiment_analysis_text.txt')
topfreq = sorted(freq.iteritems(), key=lambda x:-x[1])[:10]
for x in topfreq:
    print "{0}: {1}".format(*x)
