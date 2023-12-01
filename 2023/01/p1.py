import sys



sum=0

for line in sys.stdin:
    line = line.rstrip()
    a = b = -1
    l = len(line)
    for i in range(l):
        if a == -1 and line[i].isnumeric():
            a = int(line[i])

        if b == -1 and line[l-i-1].isnumeric():
            b = int(line[l-i-1])
    sum = sum + 10*a + b
print(sum)
