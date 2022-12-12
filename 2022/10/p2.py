import sys

def printa (x, pos, r):
    print("Sprint: ", end="")
    for i in range(40):
        print("#" if i>= x-1 and i<=x+1 else ".", end="")
    print("\nstarting cycle", pos, " X = ", x, "will print: ", "#" if r else "." )
    print("\n")


def test(x, pos):
    pos = (pos%40)
    r= pos >=(x-1) and pos<=(x+1)
    #printa(x, pos, r)
    return r
size = 300
cycle = [1]*size


input = [i.rstrip() for i in sys.stdin]

i = 1

for l in input:
    if(l[0] == 'n'):
        i=i+1
        cycle[i]=cycle[i-1]
    else:
        i=i+2
        cycle[i-1] = cycle[i-2]
        cycle[i] = cycle[i-1] + int(l.split(" ")[1])
    #print(l.split(" ")[0], cycle[max(0,i-5):i+1], i )
for t in range(i+1, size):
    cycle[t]=cycle[t-1]

print(cycle[:21])


resp = ""
for i in range(6):
    for j in range(40):
        pos = i*40 + j
        resp = resp + ( "🟥" if test(cycle[pos+1],pos) else "⬛️")
    resp= resp+ "\n"
print(resp)