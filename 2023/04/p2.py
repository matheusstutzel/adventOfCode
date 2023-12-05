import sys


c = [1]*200
for i,line in enumerate(sys.stdin):
    cards = line.strip().split(": ")[1].split(" | ")
    win = set(cards[0].split(" "))
    if '' in win:
        win.remove('')
    mine = set(cards[1].split(" "))
    points = len(win.intersection(mine))
    for j in range(points):
        c[j+i+1] = c[j+i+1] + c[i] 
    
print(sum(c[:i+1]))