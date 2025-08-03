word="carried"
num= len(word)
pairs=[]
for i in range(1,num):
    pairs.append((word[:i], word[i:]))
print (pairs)

def get_prefix(word):
    pairs=[]
    for i in range(1,num):
        pairs.append((word[:i]))
    print(pairs)

def get_suffix(word):
    pairs=[]
    for i in range(1,num):
        pairs.append((word[i:]))
    print (pairs)

import random
def random_num(word):
    pairs=[]
    num= random.randint(1, len(word))
    pairs.append((word[:num], word[num:]))
    print(pairs)

get_prefix(word)
get_suffix(word)
random_num(word)