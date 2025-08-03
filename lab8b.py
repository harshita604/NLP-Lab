# Removing punctuation, slangs and emojis

import re
from nltk.tokenize import RegexpTokenizer

slang_dict={
    "brb": "be right back",
    "lol": "laugh out loud",
    "ttyl": "talk to you later",
    "omg": "Oh my god",
    "ty": "Thank you",
    "idk": "I don't know",
    "u": "you"
}

emoji_dict={
    "😊" :"smile",
    "😂": "laugh",
    "❤️": "love",
    ":)": "smile",
    ":(": "sad",
    "😭": "cry"
}

def normalize_text(text):

    for emoji, replacement in emoji_dict.items():
        text= text.replace(emoji, f" {replacement}")
    
    tokenizer= RegexpTokenizer(r'\w+')
    words= tokenizer.tokenize(text)
    new_words=[]

    for word in words:
        clean_word= word.lower()
        new_words.append(slang_dict.get(clean_word, word))
    
    text= " ".join(new_words)
    text= text.lower()
    return text


sample = "LOL !!! This is great 😂😂, u are amazing!!!❤️"

print("Original:", sample)
print("Cleaned:", normalize_text(sample))
