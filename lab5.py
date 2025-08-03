from nltk.tokenize import regexp_tokenize
import re

def remove_digits(text):
    tokens= regexp_tokenize(text, r'\d+', gaps=True)
    text= ''.join(tokens)
    print(text)

def extract_digits(text):
    tokens= regexp_tokenize(text, r'\d+')
    print(tokens)
    print(f"Number of digits is: {len(tokens)}")

def prioritized_token(text):
    pattern= r'\b\d{1,2}/\d{1,2}/\d{2,4}\b|\b[a-zA-Z0-9+-./%]+\@[a-zA-Z0-9.-]+\.[a-zA-Z.]{2,}\b|\w+'
    tokens= regexp_tokenize(text, pattern)
    print(tokens)
text=" My friend has 2 cats, 3 dogs and 1 rabbit"
remove_digits(text)
extract_digits(text)
text2=" Send the draft on 12/05/2025 at john.doe@example.com"
prioritized_token(text2)