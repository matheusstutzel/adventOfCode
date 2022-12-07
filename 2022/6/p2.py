import sys


def solve(l):
    messageSize = 14
    for i in range(messageSize-1, len(l)):
        s = set(l)
        for j in range (messageSize):
            s.add(l[i-j])
        if(len(s)==messageSize):
            return i+1
    return 999999999999

# reading input
for line in sys.stdin:
        print(solve(line))