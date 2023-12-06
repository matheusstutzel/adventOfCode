import sys


lines = [l.strip() for l in sys.stdin]

current = [int(x) for x in lines[0][7:].split(" ")]
nxt = []
i = 2
for line in lines[2:]:
    #print(line, current, nxt)
    if len(line) ==0:
        current = nxt+current 
        nxt = []
        continue
    
    if ':' in line:
        continue
    dstart, sstart, size = [int(x.strip()) for x in line.split(" ")]
    #print(sstart, dstart, size)
    aux = []
    for v in current:
        if v>=sstart and v<sstart+size:
            nxt.append(v-sstart+dstart) 
        else:
            aux.append(v)
    current = aux
    

current = nxt+current 
print(min(current))
