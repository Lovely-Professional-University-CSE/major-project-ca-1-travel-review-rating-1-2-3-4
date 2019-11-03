import pandas as pd
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
from sklearn.feature_extraction.text import CountVectorizer
vector=CountVectorizer()
review=pd.read_csv("G:/ww.csv",encoding = 'unicode_escape')
table=str.maketrans("!@#$%^&*().,",12*" ")
data=[]
answer=[]

for index, row in review.iterrows():
    data.append(row["Review"])
    answer.append(row["Rating"])
print(answer)
for  i in range(len(data)):
    data[i]=data[i].translate(table)
vector.fit(data)
from nltk.stem.snowball import SnowballStemmer  
dat=[]
stemmer=SnowballStemmer("english")
for i in (data):
    if(stemmer.stem(i) not in stop_words):
        dat.append(stemmer.stem(i))
print(stemmer.stem("this is not a very appriated"))
bag_of_words=vector.transform(dat)
from sklearn.feature_extraction.text import TfidfTransformer
vectorizer=TfidfTransformer()
poo=vectorizer.fit_transform(bag_of_words)   
from sklearn.naive_bayes import MultinomialNB
clf=MultinomialNB().fit(poo,answer)
abc=[" terribly disappointed bad ugly disgusting","beautiful good ugly "]
tex=vector.transform(abc)
textc=vectorizer.transform(tex)
print(clf.predict(textc))

