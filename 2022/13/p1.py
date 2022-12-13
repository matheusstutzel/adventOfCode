import sys
import json


#a<b -1
#a==b 0
#a>b  1
def compareInt(a,b, pre):
    print(pre, "Compare", a,b)
    if(a==b):
        return 0 
    return 1 if a>b else -1
def compare(a,b, pre = ""):
    print(pre, "Compare", a,b)
    i = 0
    while i<len(a) and i<len(b):
        x = a[i]
        y = b[i]
        comp = 0
        if(isinstance(x,int) and isinstance(y, int)):
            comp = compareInt(x,y, pre)
        else:
            if(isinstance(x, int)):
                x = [x]
            if(isinstance(y, int)):
                y = [y]
            comp = compare(x,y, pre+"  ")
        if comp!=0:
            return comp
        i = i+1

    if i==len(a) and i == len(b):
        return 0            
    elif(i==len(a)):
        print("left side is smaller")
        return -1
    else:
        print("right side is smaller")
        return 1
    


l = [json.loads(x.strip()) for x in sys.stdin if(x!="\n")]

i = 0 
sum = 0 
while i+1< len(l):
    if(compare(l[i], l[i+1])<=0):
        print(i,i+1, "should count", i//2 +1)
        sum = sum + i//2 + 1
    else:
        print(i,i+1, "should not count", i//2 +1)
    i = i+2
print(sum)
