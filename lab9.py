import re
from nltk import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('average_perceptron_tagger_eng')
text = "The quick brown fox jumps over the lazy dog near the riverbank."

words= word_tokenize(text)
pos_tags= nltk.pos_tag(words)


for word, tag in pos_tags:
    print(f"{word:15}-> {tag}")