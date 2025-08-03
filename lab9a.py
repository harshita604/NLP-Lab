import re
import nltk

from nltk.tree import Tree
from nltk import word_tokenize, ne_chunk, pos_tag, RegexpTokenizer
nltk.download('punkt')
nltk.download('average_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')

text="Barack Obama was the 44th president of the United States. He was born in Hawaii."

tokenizer= RegexpTokenizer(r'\w+')
words= tokenizer.tokenize(text)
pos_tags= pos_tag(words)
chunks= ne_chunk(pos_tags)

print(pos_tags)
print(chunks)


entities=[]
i=0

while i< len(chunks):
    chunk= chunks[i]
    if isinstance(chunk, Tree) and chunk.label()=='PERSON':
        name= " ".join(c[0] for c in chunk)
        j= i+1
        while j< len(chunks):
            chunk_next= chunks[j]
            if isinstance(chunk_next, Tree) and chunk_next.label()=="PERSON":
                name += " " + " ".join(c[0] for c in chunk_next )
                i=j
                j+=1
            else:
                break
        entities.append((name, 'PERSON'))
    elif isinstance(chunk, Tree):
        print(chunk)
        entity_name= " ".join(c[0] for c in chunk)
        entity_label= chunk.label()
        entities.append((entity_label, entity_name))
    i+=1

print(entities)

print("\n Noun Phrases: ")

grammar= r""" NP: {<DT>?<JJ>*<NN.*>+} 
                {<NN.*>+}"""
cp = nltk.RegexpParser(grammar)
chunk_tree= cp.parse(pos_tags)

for tree in chunk_tree.subtrees(filter= lambda t: t.label()=='NP'):
    print(" ".join(name for name, tag in tree.leaves()))

chunk_tree.pretty_print()

