import sys

def hash(p):
    local = 0
    for c in p:
        local = ((local + ord(c))*17)%256
    return local

def remove(m, bucket, key):
    if bucket not in m:
        return
    b = m[bucket]
    n = []
    for k,v in b:
        if k == key:
            continue
        n.append((k,v))
    m[bucket]=n

def upsert(m, bucket, key, value):
    if bucket not in m:
        m[bucket] = []
    b = m[bucket]
    n = []
    add = False
    for k,v in b:
        if k == key:
            n.append((k,value))
            add = True
        else:
            n.append((k,v))
    if not add:
        n.append((key,value))
    m[bucket]=n

lines = [l.strip().split(",") for l in sys.stdin]

m = {}


for p in lines[0]:
    if '-' == p[-1]:
        key = p[:-1]
        bucket = hash(key)
        remove(m, bucket, key)
    else:
        key,value = p.split("=")
        bucket = hash(key)
        upsert(m, bucket, key, value)

total = 0
for k, v in m.items():
    for i,x in enumerate(v):
        total = total + (k+1)*(i+1)*int(x[1])
print(total)