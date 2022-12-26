from itertools import cycle
import sys

def top(x):
    resp = []
    for i in range(heightPattern):
        resp.extend(tab[x-i])
    return tuple(resp)

def apply(pice, x,y, clean = False):
    for i in pice:
        aux = y-1
        for j in i:
            aux = aux +1
            if(j==" "):
                continue
            tab[x][aux]= j if not clean else "."
        x= x-1

def check(pice, x, y):
    #print("check", pice, x,y)
    size = len(pice)
    if(y<0 or y+len(pice[0])>7 or (x-size+1)<0):
        #print("fora do mapa")
        return False
    for i in pice:
        aux = y-1
        for j in i:
            aux = aux +1
            #print(x,aux, j, tab[x][aux])
            if j!=" " and tab[x][aux]!=".":
                #print("bateu")
                return False
        x = x -1
    return True

def printTab(pice=None):
    if pice:
        p,x,y = pice
        apply(p,x,y)

    first = True
    for i in range(len(tab)):
        row = tab[-1-i]
        if(first and row==['.']*7):
            continue
        else: 
            first=False
        print("|"+"".join(row)+"|")
    print("+-------+")
    if(pice):
        p,x,y = pice
        apply(p,x,y, True)


tab = []
for i in range(14*2022):
    tab.append(['.']*7)

l = sys.stdin.readline().strip()
mov = cycle(l)

height = 0 



pices = [
    ["####"],

    [" # ",  #
     "###", 
     " # "],

    ["  #", 
     "  #",
     "###"],

    ["#", #
     "#",
     "#",
     "#"],

    ["##",  #
     "##"]
]

MAX = 1_000_000_000_000
heightPattern = 20
jet = 0
patMap = dict()
found = False
skipI = 0
skipH = 0 

for i in range(MAX):
    if (i + skipI) >= MAX:
        break
    #print("height", height, i, 1514285714288)
    pice = pices[i%5]
    y = 2
    x = height+2+len(pice)
    #printTab((pice, x, y))
    for m in mov: #endless loop
        ny = y + (-1 if m=='<' else 1)
        #printTab((pice, x, y))
        if(check(pice, x,ny)):
            y=ny
        jet = jet+1
        #printTab((pice, x, y))
        if(check(pice, x-1, y)):
            x=x-1
            #printTab((pice, x, y))
        else:
            break
    apply(pice, x,y)
    #print("height", height, x, len(pice))
    height = max(height,x+1)
    if jet > len(l) and not found:
        pat = (jet%len(l), i%5, top(x))
        if pat not in patMap:
            patMap[pat] = (height,i)
            continue
        found = True
        lastHeight , lastI = patMap[pat]
        diffHeigh = height - lastHeight
        diffI = i - lastI

        remain = MAX - i
        if(remain < diffI):
            continue

        skip = remain // diffI

        remain = remain % diffI
        skipH = diffHeigh * skip
        skipI = (MAX - remain)-i
        print("skip", skipH, skipI)
print(i+skipI)
print(height + skipH)

#1591860465110