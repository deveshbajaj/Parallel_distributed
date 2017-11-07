#!/usr/bin/env python2
import sys
import re

stop = {'some', 'ourselves', 'then', 'this', 'yourselves', 'aren', 'were', 'into', 'on', 'can', 'the', 'own', 'hasn', 'at', 'where', 'wasn', 't', 
'is', 'during', 'shouldn', 'in', 'off', 'both', 'y', 'up', 'isn', 'few', 'of', 'with', 'do', 'ours', 
'it', 'its', 'about', 'too', 'he', 'myself', 'your', 'by', 'mustn', 'hers', 'should', 'but', 'that', 'i', 
'for', 'further', 'his', 'don', 'other', 'our', 'again', 'm', 'will', 'd', 'needn', 'weren', 'was', 'as', 'shan', 'himself', 'these', 'and', 'you', 
'has', 'to', 'now', 'll', 'who', 'no', 've', 'just', 's', 'having', 'mightn',
'wouldn', 'my', 'whom', 'while', 'have', 'her', 'doing', 'against', 'once',
'haven', 'what', 'doesn', 'above', 'more', 'which', 'below', 'a', 'each', 'between', 'from', 'hadn', 'any', 'herself', 'same', 'they', 'themselves', 
'we', 'being', 'out', 'theirs', 'through', 'only', 'when', 'so', 'if', 'an', 'had', 'their', 
'itself', 'couldn', 'did', 'why', 'or', 'such', 'yourself', 'nor', 'over', 'ma', 'them', 'been', 'am', 'there', 'after', 'down', 'not', 'most', 'won', 'o', 'does', 'because', 'yours', 
'are', 'be', 'how', 'him', 'until', 'than', 'those', 'very', 'here', 'she', 'under', 'before', 're', 'ain', 'me', 'didn', 'all'}

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
   
    line = re.sub(r'[^\w\s]','',line)
    

    #word_tokens = word_tokenize(line)
    word_tokens = list(line.split(" "))
    filtered_sentence = [w for w in word_tokens if not w in stop]
    final = ' '.join(filtered_sentence)  
    print(final)



