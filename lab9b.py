import spacy
import nltk

nlp= spacy.load('xx_ent_wiki_sm')
#nlp= spacy.load('en_core_web_sm')
text="Barack Obama was the 44th president of the United States. He was born in Hawaii."
tokenizer= nltk.RegexpTokenizer(r'\w+')
tokens= tokenizer.tokenize(text)
text= " ".join(tokens)
doc= nlp(text)

for token in doc:
    print(f" {token.text:15} -> POS/ {token.pos_:5} TAG /{token.tag_:5} Dep/ {token.dep_}")

for np in doc.noun_chunks:
    print(np.text)

for ent in doc.ents:
    print(f"{ent.text:15}- {ent.label_}")