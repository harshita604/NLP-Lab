import re
def remove_nonaplhanum(text):
    pattern= r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$'
    print (re.sub(pattern, '', text))

def count_nonalphanum(text):
    pattern=r'[^a-zA-Z0-9"\s]'
    char= re.findall(pattern, text)
    print (len(char))

def replace_nonalphanum(text):
    pattern=r'[^a-zA-Z0-9"\s]'
    replacement_char="_"
    print (re.sub(pattern, replacement_char, text))

text="???Hello World!!!!"
remove_nonaplhanum(text)
count_nonalphanum(text)
replace_nonalphanum(text)