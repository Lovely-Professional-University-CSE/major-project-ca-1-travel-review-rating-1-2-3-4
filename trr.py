

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
   


    content=f
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

        ### project part 2: comment out the line below
        words = text_string

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        




    return words


from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import  stopwords
from nltk.stem.snowball import SnowballStemmer  
import nltk
#nltk.download()
stemmer=SnowballStemmer("english")
a=stemmer.stem("unreponsive")
print(a)     
vectorize=      CountVectorizer()
string1="this is a great hotel loved the stay here."
string2="room service is very bad and late."
print(parseOutText(string1))
relist=[string1,string2]
bagwords=vectorize.fit(relist) 
bagwords=vectorize.transform(relist)

print(bagwords)