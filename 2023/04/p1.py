import sys


sum = 0
for line in sys.stdin:
    cards = line.strip().split(": ")[1].split(" | ")
    win = set(cards[0].split(" "))
    if '' in win:
        win.remove('')
    mine = set(cards[1].split(" "))
    points = len(win.intersection(mine))-1
    sum = sum +( 2**points if points>=0 else 0)
print(sum)