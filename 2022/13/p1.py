import sys
import json

def compareInt(a,b):
    if(a==b):
        return 0 
    return 1 if a>b else -1
def compare(a,b):
    i = 0
    while i<len(a) and i<len(b):
        x = a[i]
        y = b[i]
        comp = 0
        if(isinstance(x,int) and isinstance(y, int)):
            comp = compareInt(x,y)
        else:
            if(isinstance(x, int)):
                x = [x]
            if(isinstance(y, int)):
                y = [y]
            comp = compare(x,y)
        if comp!=0:
            return comp
        i = i+1

    if i==len(a) and i == len(b):
        return 0            
    elif(i==len(a)):
        return -1
    else:
        return 1
    


l = [json.loads(x.strip()) for x in sys.stdin if(x!="\n")]

i = 0 
sum = 0 
while i+1< len(l):
    if(compare(l[i], l[i+1])<=0):
        sum = sum + i//2 + 1
    i = i+2
print(sum)
