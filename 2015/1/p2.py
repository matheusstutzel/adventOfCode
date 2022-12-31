import sys

l = [[1 if c=='(' else -1 for c in l.strip()] for l in sys.stdin]
for i in l:
    pos = 0
    for idx,c in enumerate(i):
        pos = pos + c
        if(pos<0):
            print(idx+1)
            break