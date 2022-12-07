import sys


def solve(l):
    for i in range(3, len(l)):
        s = set()
        for j in range (4):
            s.add(l[i-j])
        if(len(s)==4):
            return i+1
    return 999999999999

# reading input
for line in sys.stdin:
        print(solve(line))