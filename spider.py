# -*- coding: utf-8 -*-
#coding:utf-8
import string
import urllib
from bs4 import BeautifulSoup
import os
import re
import nltk
import chardet
from nltk.stem.porter import *
from nltk.corpus import stopwords


def getText(url, localpath):
    files = os.listdir(url)
    it = int(0)
    for file in files:
        htmlfile = open(url+"\\"+file, 'rb')
        htmlpage = htmlfile.read()

        soup = BeautifulSoup(htmlpage, "html.parser")
        print(soup.title.string)



        level = soup.findAll(name='div', attrs={"class": re.compile(r'^levelBadge badge')})
        post = soup.findAll(name='div', attrs={"class": "postBody"})
        date = soup.findAll(name='div', attrs={"class": "postDate"})[0].text
        date = date[date.find(",")-4:date.find(",")]
        it += 1
        print(it)
        for a in range(len(post)):
            if a > 0:
                 t=post[a].select('p')
                 if len(post)-len(level)>1:
                     break
                 if len(post)-len(level)==1:
                     l=level[a-1].attrs["class"]
                 else:
                     l=level[a].attrs["class"]
                 n = ""
                 for c in l:
                     n = n+c
                 filepath = os.path.join(localpath, date)
                 if os.path.exists(filepath) == False:
                     os.makedirs(filepath)
                 fp = open(filepath + '.txt', 'a', encoding='utf-8')
                 for b in range(len(t)):
                    section_text = t[b].text
                    sentence = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", " ", section_text)
                    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
                    sentence = sentence.translate(remove_punctuation_map)
                    sentence = sentence.lower()
                    sentence=nltk.word_tokenize(sentence)
                    sentence = [w for w in sentence if not w in stopwords.words('english')]
                    wordnet_lemmatizer = nltk.WordNetLemmatizer()
                    sentence = stem_tokens(sentence, wordnet_lemmatizer)
                    sentence=' '.join(sentence)
                    # sentence= bytes(sentence, 'utf-8')
                    # encode_type = chardet.detect(sentence)
                    # if encode_type['encoding'] != None:
                    #     sentence = sentence.decode(encode_type['encoding'])
                    # sentence=str(sentence)
                    fp.write(sentence)
                 fp.write(","+"\n")
            # text = soup.select('.postBody p')[1].text
    # level[1].attrs['class']

    return None

def stem_tokens(tokens, wordnet_lemmatizer):
    stemmed = []
    for item in tokens:
        stemmed.append(wordnet_lemmatizer.lemmatize(item))
    return stemmed


url = r'D:\DarwinTravel'
localPath = r'D:\Result7'
getText(url, localPath)

