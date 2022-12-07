import sys


def value(c):
    v = ord(c)
    if(v>90):
        return v - ord('a') + 1 
    else:
        return v - ord('A') + 27

def convert(l):
    i = 0 
    for c in l:
        #each letter represented from 1 to 52
        v = value(c)
        #"accumulates" the letters
        i = i | (1<<v)
    return i

# 64 bit all one
c = 0xFFFFFFFFFFFFFFFF
i = 0
t = 0


# reading input
for line in sys.stdin:
    #group every 3 
    if i == 3:
        # https://stackoverflow.com/a/36059264/4406989 
        # find first [bit] set 
        t = t + c.bit_length()-1
        c = 0xFFFFFFFFFFFFFFFF
        i = 0
        
    
    l = line.rstrip()
    v = convert(l)
    #keep only bits in both "words"
    c = c&v
    i = i +1

#consider last group
t = t + c.bit_length()-1

    

print(t)
