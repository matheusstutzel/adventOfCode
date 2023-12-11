import sys

def nextNumber(n):
    if len(n) == 0:
         return 0
    k = [n[i+1]-n[i] for i in range(len(n)-1)]
    return n[0] - nextNumber(k)


input = [l.strip() for l in sys.stdin]

total = 0
for i in input:
    numbers = [int(x) for x in i.split()]
    next = nextNumber(numbers)
    total = total + next
print(total)