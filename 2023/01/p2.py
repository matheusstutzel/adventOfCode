import sys


names = ["one","two","three","four","five","six","seven","eight","nine"]
firstLetters = set(["o","t","f","s","e","n"])
def parse(s):
    if s[0].isnumeric():
        return int(s[0])
    if s[0] not in firstLetters:
        return -1
    for idx,name in enumerate(names):
        if s.startswith(name):
            return idx+1
    return -1

sum=0

for line in sys.stdin:
    line = line.rstrip()
    a = b = -1
    l = len(line)
    for i in range(l):
        if a == -1:
            a = parse(line[i:])

        if b == -1:
            b = parse(line[l-i-1:])
    sum = sum + 10*a + b
print(sum)
