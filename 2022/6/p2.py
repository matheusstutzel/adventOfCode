import sys


def solve(l,messageSize):
    for i in range(messageSize, len(l)):
        s = set(l[i-messageSize:i])
        if(len(s)==messageSize):
            return i
    return 999999999999

# reading input
for line in sys.stdin:
        print(solve(line,14))