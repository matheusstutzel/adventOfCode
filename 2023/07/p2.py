import sys
from functools import cmp_to_key
from collections import defaultdict

ref = 'AKQT98765432J' 

def isFullHouse(mmax, a,c):
    if mmax != 3:
        return False
    if 'J' in a:
        fullHouse = True
        for k,v in c.items():
            if k == 'J':
                continue
            fullHouse = fullHouse and v == 2
        return fullHouse
    return 2 in c.values() and 3 in c.values()
def extractInfo(a):
    mmax = 0
    c = defaultdict(int)
    for k in a:
        c[k] = c[k]+1
        if(k == 'J'):
            continue
        mmax = max(mmax, c[k])
    mmax = mmax + c['J']

    fullHouse = isFullHouse(mmax, a, c)
    if fullHouse:
        return 3.5
    pairs = sum([1 if v==2 else 0 for v in c.values()])
    if c['J'] == 2:
        pairs = pairs -1
    if mmax == 2 and pairs ==0:
        pairs = 1
    if pairs == 2:
        mmax = 2.5
    return mmax

def hands_cmp(a,b):
    maxA = extractInfo(a[0])
    maxB = extractInfo(b[0])
    if maxA != maxB:
        return maxA-maxB

    for i in range(5):
        A = a[0][i]
        B = b[0][i]
        if A == B:
            continue   
        return ref.find(B) - ref.find(A)
    return 0

hands_cmp_key = cmp_to_key(hands_cmp)
hands = [l.strip().split() for l in sys.stdin]
hands.sort(key=hands_cmp_key)
result = 0
i = 1
for k,v in hands:
    result = result + i*int(v)
    i = i+1
print(result)

