import sys

def test(k,v):
    if v[0]>k:
        return False
    if len(v)==1:
        return v[0]==k
    if(test(k, [v[0]+v[1]]+v[2:])):
        return True
    if(test(k, [v[0]*v[1]]+v[2:])):
        return True
    return False
        

sum=0

for l in sys.stdin:
    expected,rest=l.rstrip().split(":")
    v=[int(x.strip()) for x in rest.strip().split()]
    k=int(expected)
    if(test(k,v)):
        sum+=k
print(sum)
