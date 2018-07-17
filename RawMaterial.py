# -*- coding: utf-8 -*-
#coding:utf-8
import string
import urllib
from bs4 import BeautifulSoup
import os
import re

import chardet
def getText(url, localpath):
    files = os.listdir(url)
    it = int(0)
    for file in files:
        #htmlfile = open(url+"\\"+file, 'rb')
        #htmlpage = htmlfile.read()
        #soup = BeautifulSoup(htmlpage, "html.parser")
       # print(soup.title.string)





        #date = soup.findAll(name='div', attrs={"class": "postDate"})[0].text
        #date = date[date.find(",")-4:date.find(",")]
        it += 1
        print(it)



        #filepath = os.path.join(localpath, date)
        if os.path.exists(localpath) == False:
         os.makedirs(localpath)
        fp = open(localpath+"\ total.txt", 'a', encoding='utf-8')
        for line in open(url+"\\"+file, 'r', encoding="utf-8"):
            # sentence=line
            # sentence = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", " ", sentence)
            # remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
            # sentence = sentence.translate(remove_punctuation_map)
            fp.writelines(line)
        fp.write("\n")
            # text = soup.select('.postBody p')[1].text
    # level[1].attrs['class']

    return None


url = r'D:\Darwintest'
localPath = r'D:\RawResult7'
getText(url, localPath)

