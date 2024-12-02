import sys

def safe(s):
    return len(s.difference({-1,-2,-3})) == 0 or len(s.difference({1,2,3}))==0

result = 0 
for l in sys.stdin:
    v = [int(x) for x in l.split()]
    diff = set([v[i+1]-v[i] for i in range(len(v)-1)])
    if(safe(diff)):
        result +=1
print(result)
