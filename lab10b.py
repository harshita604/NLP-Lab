from hmmlearn import hmm
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from collections import Counter, defaultdict
import nltk
import re
from nltk.tokenize import RegexpTokenizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('punkt')
categories= ['comp.graphics', 'sci.space', 'rec.sport.hockey']
data= fetch_20newsgroups(subset='all', categories= categories)
texts, labels= data.data, data.target

def clean(text):
    text= text.lower()
    text= re.sub(r'\d+',' ', text)
    tokenizer= RegexpTokenizer(r'\w+')
    tokens= tokenizer.tokenize(text)
    return [token for token in tokens if token.isalpha()]

tokenized_texts= [clean(text) for text in texts]
filtered= [(t,l) for t,l in zip(tokenized_texts, labels) if len(t)>0 ]
tokenized_texts, labels= zip(*filtered)

X_train, X_test, y_train, y_test= train_test_split(tokenized_texts, labels, test_size=0.2, random_state=42)

all_words= Counter(word for text in tokenized_texts for word in text )
word2idx= {word:idx for idx, (word, _) in enumerate(all_words.items())}

def encode(text):
    return [word2idx.get(word,0) for word in text if word in word2idx]

X_train_encoded= [encode(text) for text in X_train]
X_test_encoded= [encode(text) for text in X_test]

train_data= [(t,y) for t,y in zip(X_train_encoded, y_train) if len(t)>0 ]
test_data= [(t,y) for t,y in zip(X_test_encoded, y_test) if len(t)>0]
X_train_encoded, y_train= zip(*train_data)
X_test_encoded, y_test= zip(*test_data)

encoder= LabelEncoder()
y_train_labels= encoder.fit_transform(y_train)
y_test_labels= encoder.fit_transform(y_test)

class_sequences= defaultdict(list)
for label, sequence in zip(y_train_labels, X_train_encoded):
    class_sequences[label].append(sequence)

class_hmms={}

for label, sequences in class_sequences.items():
    X= np.concatenate([np.array(seq).reshape(-1,1) for seq in sequences])
    length= [len(seq) for seq in sequences]
    model= hmm.MultinomialHMM(n_components=6, n_iter=100)
    model.fit(X, length)

    class_hmms[label]= model

def features(encoded_text):
    features= []
    for seq in encoded_text:
        X= np.array(seq).reshape(-1,1)
        probs=[]
        for labels in sorted(class_hmms.keys()):
            score= class_hmms[label].score(X)
            probs.append(score)
        features.append(probs)
    return np.array(features)


X_train_hmm= features(X_train_encoded)
X_test_hmm= features(X_test_encoded)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_train_hmm_scaled = scaler.fit_transform(X_train_hmm)
X_test_hmm_scaled = scaler.transform(X_test_hmm)

model= MultinomialNB()
model.fit(X_train_hmm_scaled, y_train_labels)
y_pred= model.predict(X_test_hmm_scaled)

acc = accuracy_score(y_test_labels, y_pred)
precision, recall, f1, _ = precision_recall_fscore_support(y_test_labels, y_pred, average='macro')
print("\n=== Hybrid HMM + Naive Bayes Evaluation ===")
print(f"Accuracy:  {acc:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score:  {f1:.4f}")

