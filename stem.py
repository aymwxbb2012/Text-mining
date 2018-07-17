# coding=utf-8

import nltk
import math
import string
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer
import os
def getFilelist(path) :
    filelist = []
    files = os.listdir(path)
    for f in files:
        if(f[0] == '.'):
            pass
        else:
            filelist.append(f)
    return filelist, path


def getTextList(filelist,path):

    path=path+"\\"
    corpus = []
    for ff in filelist:
        fname = path + ff
        f = open(fname, 'r+')
        content = f.read()
        f.close()
        corpus.append(content)

    return corpus

def get_tokens(text):
        #lowers = text.lower()
        #remove the punctuation using the character deletion step of translate
        remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
        no_punctuation = text.translate(remove_punctuation_map)
        tokens = nltk.word_tokenize(no_punctuation)
        return tokens


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed



if __name__ == "__main__" :

    path = r'D:\RawResult4\ total.txt'
    file = open(path, 'r', encoding='utf-8')
    text=file.read();
    tokens=get_tokens(text)
    # (allfile, path) = getFilelist(path)
    # textlist=getTextList(allfile,path)
    #
    # tokens = get_tokens(textlist[0])
    # filtered = [w for w in tokens if not w in stopwords.words('english')]
    # stemmer = PorterStemmer()
    # stemmed = stem_tokens(filtered, stemmer)
    count = Counter(tokens)
    print(count)