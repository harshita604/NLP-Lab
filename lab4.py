from collections import Counter
from nltk.util import ngrams

def get_ngram_frequencies(text):
    words= text.split()
    num= len(words)
    for i in range(num):
        n_gram= list(ngrams(words,i))
        frequencies= Counter(n_gram)
        for gram, freq in frequencies.items():
            print(f"For {i}-gram:\n {gram}:{freq}")

def get_ngram_probabilities(text):
    words= text.split()
    for i in range (len(words)):
        n_gram= list(ngrams(words,i))
        frequencies= Counter(n_gram)
        total= len(n_gram)
        probabilities={gram:freq/total for gram, freq in frequencies.items()}
        for gram, prob in probabilities.items():
            print(f"The probability of {i}-gram:\n {gram}:{prob}")

def reverse_ngram(text):
    words= text.split()[::-1]
    n_gram= list(ngrams(words,2))
    frequencies= Counter(n_gram)
    print(n_gram)
    for gram, freq in frequencies.items():
        print(f"The bigram:\n {gram}:{freq}")

text= "This is a sample sentence."
get_ngram_frequencies(text)
get_ngram_probabilities(text)
reverse_ngram(text)
