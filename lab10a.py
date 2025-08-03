import nltk
import re
from nltk.tokenize import word_tokenize, RegexpTokenizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, accuracy_score, recall_score, f1_score, precision_recall_fscore_support
from hmmlearn import hmm 
from collections import Counter, defaultdict
import numpy as np

nltk.download('punkt')

def clean(text):
    text= text.lower()
    text= re.sub(r'\d+', ' ', text)
    tokenizer= RegexpTokenizer(r'\w+')
    tokens= tokenizer.tokenize(text)
    return [token for token in tokens if token.isalpha()]

categories= ['comp.graphics','sci.space','rec.sport.hockey']
data= fetch_20newsgroups(subset='all', categories=categories)
texts, labels= data.data, data.target
label_names= data.target_names

tokenized_texts= [clean(text) for text in texts]

filtered= [(t,l) for t,l in zip(tokenized_texts, labels) if len(t)>0]
tokenized_texts, labels= zip(*filtered)

X_train, X_test, y_train, y_test= train_test_split(tokenized_texts, labels, test_size=0.2, random_state=42)

# Enocde text
word_counter= Counter(word for text in tokenized_texts for word in text)
word2idx= {word:idx for idx, (word,_) in enumerate(word_counter.items())}

def encode_text(text):
   return [word2idx.get(word, 0) for word in text if word in word2idx]

X_train_encoded= [encode_text(text) for text in X_train]
X_test_encoded= [encode_text(text) for text in X_test]

train_data= [(x,y) for x,y in zip(X_train_encoded, y_train) if len(x)>0]
test_data= [(x,y)for x,y in zip(X_test_encoded, y_test) if len(x)>0]
X_train_encoded, y_train= zip(*train_data)
X_test_encoded, y_test= zip(*test_data)

encoder= LabelEncoder()
y_train_labels= encoder.fit_transform(y_train)
y_test_labels= encoder.fit_transform(y_test)

class_sequences= defaultdict(list)

for seq, label in zip(X_train_encoded, y_train_labels):
    class_sequences[label].append(seq)

class_hmms={}
for labels, sequences in class_sequences.items():
    lengths= [len(seq)for seq in sequences]
    X= np.concatenate([np.array(seq).reshape(-1,1) for seq in sequences])

    model= hmm.MultinomialHMM(n_components=6, n_iter=42)
    model.fit(X, lengths)
    class_hmms[label]= model


def predict(text):
    seq= np.array([[word2idx.get(word,0)] for word in text if word in word2idx])
    if len(seq)==0:
        return -1
    scores={}
    for label, model in class_hmms.items():
        scores[label]= model.score(seq)/ len(seq)

    return max(scores, key=scores.get)

y_pred= [predict(text) for text in X_test]    
y_true=  y_test_labels

y_pred_filtered = [pred for pred in y_pred if pred!=-1]
y_true_filtered= [true for true, pred in zip(y_true, y_pred) if pred!=-1]
acc = accuracy_score(y_true_filtered, y_pred_filtered)
precision, recall, f1, _ = precision_recall_fscore_support(y_true_filtered, y_pred_filtered, average='macro')

print(" Evaluation Metrics")
print(f"Accuracy:  {acc:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score:  {f1:.4f}")

# Show predictions for first 10 test examples
print("\n Sample Predictions:\n")
for i in range(10):
    text= X_test[i]
    label= encoder.inverse_transform([y_test_labels[i]])[0]
    predicted_label= predict(text)
    pred= encoder.inverse_transform([predicted_label])[0]

    input= " ".join(text)[:200].replace("\n", " ")
    print(f"\n Input : {input}")
    print(f"\n Predicted: {pred}")
    print(f"\n True : {label}")
    print("************************************************")
