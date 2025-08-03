import numpy as np
from hmmlearn import hmm 

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

documents=[
    ("I love this movie", "positive"),
    ("This film is terrible", "negative"),
    ("Great acting and plot", "positive"),
    ("Horrible direction and script", "negative")
]

texts, labels= zip(*documents)

tokenized_texts= [word_tokenize(text.lower()) for text in texts]

all_words= set(word for text in tokenized_texts for word in text)
word2idx= {word:idx for idx, word in enumerate(all_words)}
encoded_texts=[[word2idx[word] for word in text] for text in tokenized_texts]

encoder= LabelEncoder()
encoded_labels= encoder.fit_transform(labels)
class_hmms= {}
for label in set(encoded_labels):
    sequences= [encoded_texts[i] for i in range(len(encoded_labels)) if encoded_labels[i]== label]
    X= np.concatenate([np.array(seq).reshape(-1,1) for seq in sequences])
    lengths= [len(seq) for seq in sequences]

    model= hmm.MultinomialHMM(n_components=3, n_iter=100)
    model.fit(X, lengths)
    class_hmms[label]= model

def predict(text):
    tokens= word_tokenize(text.lower())
    encoded= np.array([[word2idx.get(word, 0)] for word in tokens])
    scores= {}

    for label, model in class_hmms.items():
        try:
            scores[label]= model.score(encoded)/ len(encoded)
        except:
            scores[label]= float('-inf')
    
    best_label= max(scores, key= scores.get)
    return encoder.inverse_transform([best_label])[0]

print(predict("This movie is amazing"))
print(predict("Worst movie ever"))
    