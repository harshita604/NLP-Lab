import nltk
import re
from nltk import word_tokenize, pos_tag,  ne_chunk
from nltk.tree import Tree

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

def normalize_text(text):
    text= re.sub(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b', 'DATE', text)
    text= re.sub(r'\$\d+(?:,\d{3})*(?:\.\d{2})?', 'MONEY', text)
    text= re.sub(r'\b\d+\b', 'NUMBER', text)
    return text

def extract_ner(text):
    tokens= word_tokenize(text)
    pos_tags= pos_tag(tokens)
    chunks= ne_chunk(pos_tags)
    entities= []
    for chunk in chunks:
        if isinstance(chunk, Tree):
            entity_name= " ".join(c[0] for c in chunk)
            entity_label= chunk.label()
            entities.append((entity_name, entity_label))
    return entities         

text = "Barack Obama was born on 04/08/1961 and earned $400000 annually as President of the United States."
normalized_text = normalize_text(text)
entities = extract_ner(normalized_text)

print("Normalized Text:", normalized_text)
print("Named Entities:", entities)







