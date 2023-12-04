import sys

maxV = {
    "r":12,
    "g": 13,
    "b": 14
}

def possible(l):
    for w in l.split(","):
        count, color = w.strip().split(" ")
        count = int(count)
        if count > maxV[color[0]]:
            return False
    return True
sum=0

for line in sys.stdin:
    line = line.strip()
    game, x = line.split(':')
    game = int(game[5:])
    result = all([possible(k.strip()) for k in x.split(";")])
    sum = sum + (game if result else 0)
print(sum)