import sys

def convert(l): # could be removed 
    return "".join([chr(i+ord('m')) for i in l])
def calc(x, r):
    seq = []
    diff=[]
    for i in range(r):
        a = x%10
        x = (x^(x*64)) %16777216
        x = (x^(x//32))%16777216
        x = (x^(x*2048)) %16777216
        diff.append((x%10)-a)
        seq.append(x%10)        
    return x, seq,convert(diff)
l =[int(l.strip()) for l in sys.stdin]

dic={}
for x in l:
    y,seq,diff = calc(x, 2000)
    seen = set()
    for i in range(len(diff)-3):
        pat = diff[i:i+4]
        point = seq[i+3]
        if pat not in seen:
            seen.add(pat)
            if pat not in dic:
                dic[pat]=0
            dic[pat]+=point
    #print(x,y)

print(max([dic[x] for x in dic ]))
