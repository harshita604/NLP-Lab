import re
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

def normalize_text(text):
    pattern= r'http\S+|www\S+|https\S+'
    text= re.sub(pattern, '', text)
    text= re.sub(r'[#@]','', text)

    tokenizer= RegexpTokenizer(r'\w+')
    tokens= tokenizer.tokenize(text.lower())

    tokens= [word for word in tokens if word not in stopwords.words('english')]
    return tokens

def stem_lemmatize(tokens):
    stemmer= PorterStemmer()
    lemmatizer= WordNetLemmatizer()

    stemmed= [stemmer.stem(word) for word in tokens]
    lemmatized= [lemmatizer.lemmatize(word) for word in tokens]

    return stemmed, lemmatized

text = "Check out our new AI-powered service at https://example.com! , www.example.com @OpenAI #AI #ML"
tokens= normalize_text(text)
print(tokens)
stemmed, lemmatized= stem_lemmatize(tokens)
print("\n Stemmed: \t ", stemmed)
print("\n Lemmatized: " ,lemmatized)








