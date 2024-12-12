import sys
l = [[int(x) for x in l.strip().split()] for l in sys.stdin][0]


def simulate(l):
    result = []
    for x in l:
        if x == 0:
            result.append(1)
            continue
        s = str(x)
        if len(s)%2==0:
            result.append(int(s[:len(s)//2]))
            result.append(int(s[len(s)//2:]))
            continue
        result.append(x*2024)        
    return result

#print(l)
for i in range(25):
    l = simulate(l)
    #print(len(l))
print(len(l))
