import sys

def resolve(val, lazy, key):
    if key not in val and key not in lazy:
        return None
    if key in val:
        return val[key]
    a,op,b = lazy[key]
    a = resolve(val, lazy, a)
    b = resolve(val, lazy, b)
    if op == "AND":
        return a&b
    if op== "XOR":
        return a^b
    if op=="OR":
        return a|b
    raise Exception("error "+op)
    
val={}

l=input()
while l!="":
    x,v= l.strip().split(": ")
    val[x]=int(v)
    l = input()

lazy = {}
for l in sys.stdin:
    x,v = l.strip().split(" -> ")
    lazy[v]=x.split()
result=""
z=0
while True:
    r = resolve(val, lazy, f"z{z:02d}")
    if r==None:
        break
    result =  str(r)+result
    z+=1
print(result, int(result, 2))
    
