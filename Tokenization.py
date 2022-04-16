import sys
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
f=open("orangereview.txt").read()
sentences=sent_tokenize(f)
my_sentence=[sent for sent in sentences if 'company' in word_tokenize(sent)]
sys.stdout=open("orange_company.txt","w")


print my_sentence

