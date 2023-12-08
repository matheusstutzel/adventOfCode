import sys
from functools import cmp_to_key
from collections import defaultdict

ref = 'AKQJT98765432' 

def extractInfo(a):
    mmax = 0
    c = defaultdict(int)
    for k in a:
        c[k] = c[k]+1
        mmax = max(mmax, c[k])
    return (mmax, sum([1 if v==2 else 0 for (k,v) in c.items()]))

def hands_cmp(a,b):
    maxA, pairsA = extractInfo(a[0])
    maxB, pairsB = extractInfo(b[0])
    if maxA != maxB:
        return maxA-maxB

    if pairsA != pairsB:
        return pairsA - pairsB

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
