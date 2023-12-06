import sys


lines = [l.strip() for l in sys.stdin]

aux = [int(x) for x in lines[0][7:].split(" ")]
current = []
for i in range(0,len(aux),2):
    current.append((aux[i], aux[i]+aux[i+1]-1))
print(current)

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
    send = sstart+size
    diff = dstart-sstart
    #print(sstart, dstart, size)
    aux = []
    for a,b in current:
        # Before
        #   .....
        #         ......
        # or After
        #         ......
        #   .....
        if (b<sstart) or (a>=send):
            aux.append((a,b))
            continue
        # Before with intersec
        #   .....
        #      ......
        if (a<sstart and b<send):
            aux.append((a, sstart-1))
            nxt.append((sstart+diff, b+diff))
            continue
        # After with intersec
        #      ......
        #   .....
        if (a<send and b>=send):
            aux.append((a,send-1))
            nxt.append((send+diff, b+diff))
            continue  
        # within
        #      ......
        #   ............
        if (a>=sstart and b<send):
            nxt.append((a+diff, b+diff))
            continue
        # bigger
        #   ............            
        #      ......
        if (a<sstart and b>=send):
            aux.append((a,sstart-1))
            aux.append((send,b))
            nxt.append((sstart+diff, send+diff))
            continue
        
        print(sstart, send, a,b)
        raise Exception("dunno ")
    current = aux
    

current = nxt+current 
print(min(current)[0])