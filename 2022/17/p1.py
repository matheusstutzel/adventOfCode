from itertools import cycle
import sys

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


for i in range(2022):
    #print("height", height)
    pice = pices[i%5]
    y = 2
    x = height+2+len(pice)
    #printTab((pice, x, y))
    for m in mov: #endless loop
        ny = y + (-1 if m=='<' else 1)
        #printTab((pice, x, y))
        if(check(pice, x,ny)):
            y=ny
        #printTab((pice, x, y))
        if(check(pice, x-1, y)):
            x=x-1
            #printTab((pice, x, y))
        else:
            break
    apply(pice, x,y)
    #print("height", height, x, len(pice))
    height = max(height,x+1)


    
print(height)    