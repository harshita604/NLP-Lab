import nltk
import re
text="This is a sample text, with som punctuation??. Also new lines and carriage returns, let's split it."
words= nltk.word_tokenize(text)
from nltk.tokenize import RegexpTokenizer
tokens= re.split(r'[\s\W+]', text)
print(tokens)
print(words)

def find_dates(text):
    date_patterns=[
    r'\d{1,2}/\d{1,2}/\d{2,4}',
    r'\d{1,2}-\d{1,2}-\d{2,4}',
    r'\b((?: Jan|Feb|March|April|May|June|July|Aug|Sept|Oct|Nov|Dec) \d{1,2}, \d{2,4})\b'
]
    dates=[]
    for pattern in date_patterns:
        match= re.findall(pattern,text)
        if match:
            dates.extend(match)
    return dates

def phone_numbers(text):
    phone_patterns=[
        r'\b \d{3}([-.\s])\d{3}\1\d{4}\b',
        r'\+\(\d{1,2}\)\-\d{10}',
        r'\(\d{1,2}\) \d{10}'
    ]
    numbers=[]
    for pattern in phone_patterns:
        match= re.findall(pattern, text)
        if match:
            numbers.extend(match)
    return numbers

input_text = "This is a #sample text! Remove the #hashtag and noise! Visit @example. Call me at 123 456-7890 or 987-654-3210 or +(91)-8888855555. Meet me on 12/05/2023 or June 15, 2024 😊."
print(find_dates(input_text))
print(phone_numbers(input_text))