# -*- coding: utf-8 -*-
#coding:utf-8
import urllib
from bs4 import BeautifulSoup
import os
import re
import chardet
def getText(url, localpath):
    files = os.listdir(url)
    for file in files:
        htmlfile = open(url+"\\"+file, 'rb')
        htmlpage = htmlfile.read()
    #print htmlpage
        soup = BeautifulSoup(htmlpage, "html.parser")
        print(soup.title.string)

    # cctag = soup.find_all('img', attrs={'class':'BDE_Image'})

        level = soup.findAll(name='div', attrs={"class": re.compile(r'^levelBadge badge')})
        post = soup.findAll(name='div', attrs={"class": "postBody"})
        date = soup.findAll(name='div', attrs={"class": "postDate"})[0].text
        date = date[date.find(",")-4:date.find(",")]
        print(len(post)+len(level))
        # text = post[2].select('p')
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
                 fp = open(filepath+"\ " + n + '.txt', 'a')
                 for b in range(len(t)):
                    section_text = t[b].text
                    sentence = re.sub("[+:\.\!\/_,$%^*(+\"\'<>]+|[+——！，。？、~@#￥%……&*（）]+", " ", section_text)
                    # sentence= bytes(sentence, 'utf-8')
                    # encode_type = chardet.detect(sentence)
                    # if encode_type['encoding'] != None:
                    #     sentence = sentence.decode(encode_type['encoding'])
                    # sentence=str(sentence)
                    fp.write(sentence)
                 fp.write(","+"\n")
            # text = soup.select('.postBody p')[1].text
    # level[1].attrs['class']


    # for i in cctag:
    #     print (i.attrs['src'])
    #     urllib.urlretrieve(i.attrs['src'], os.path.join(filepath, '%s'%i.attrs['src'].split('/')[-1]))
    # htmlfile.close()
    return None


url = r'D:\Darwin'
localPath = r'D:\Result'
getText(url, localPath)

