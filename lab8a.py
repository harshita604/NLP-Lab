# Remove slangs, emojis and normalize punctuations

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

abbrev_dict={
 "Mr.": "Mister",
 "Ms.": "Miss",
 "Dr.": "Doctor"

}

def normalize_text(text):

    for abbrev, replacement in abbrev_dict.items():
        pattern = re.compile(re.escape(abbrev), re.IGNORECASE)
        text = pattern.sub(replacement, text)

    for emoji, replacement in emoji_dict.items():
        text= text.replace(emoji, f" {replacement}")

    words= text.split()
    new_words=[]
    for word in words:
        clean_word= word.lower()
        new_words.append(slang_dict.get(clean_word, word))

    text= " ".join(new_words)
    text= re.sub(r'([?>!.,])\1+', r'\1', text)
    text= re.sub(r'\s+', ' ', text)
    text= re.sub(r'\s([?><!])', r'\1', text)
    text= text.lower()
    return text

sample = "LOL !!! This is great 😂😂, u are amazing!!!❤️. Thank you Dr. John"

print("Original:", sample)
print("Cleaned:", normalize_text(sample))
