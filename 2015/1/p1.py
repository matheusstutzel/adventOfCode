import sys

l = [sum([1 if c=='(' else -1 for c in l.strip()]) for l in sys.stdin]
print(l)