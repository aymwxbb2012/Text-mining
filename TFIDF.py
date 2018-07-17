

import os



from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

def getFilelist(path) :
    filelist = []
    files = os.listdir(path)
    for f in files:
        if(f[0] == '.'):
            pass
        else:
            filelist.append(f)
    return filelist, path


def Tfidf(filelist,path):

    path=path+"\\"
    corpus = []
    for ff in filelist:
        fname = path + ff
        f = open(fname, 'r+',encoding='utf-8')
        content = f.read()
        f.close()
        corpus.append(content)

    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()

    sFilePath = 'D:/tfidffile'
    if not os.path.exists(sFilePath):
        os.mkdir(sFilePath)


    for i in range(len(weight)):
        f = open(sFilePath + '/' + str.zfill(str(i), 5) + '.csv', 'w+', encoding='utf-8')
        for j in range(len(word)):
            f.write(word[j] + "," + str(weight[i][j]) + "\n")
        f.close()




if __name__ == "__main__" :
    path = r'D:\Darwintest'
    (allfile, path) = getFilelist(path)
    Tfidf(allfile,path)