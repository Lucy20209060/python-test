#!/usr/bin/python
# -*- coding: UTF-8 -*-
import nltk
import urllib.request
response = urllib.request.urlopen('http://rpa.aliyun.net/')
html = response.read()
print (html)

# sentence = """At eight o'clock on Thursday morning
# ... Arthur didn't feel very good."""
# tokens = nltk.word_tokenize(sentence)
# print (tokens)

# tagged = nltk.pos_tag(tokens)
# print(tagged[0:6])

# import nltk
from nltk.book import *
fdist1 = FreqDist(str(html))
for key in fdist1:
    print(key, fdist1[key])

fdist1.most_common(3)