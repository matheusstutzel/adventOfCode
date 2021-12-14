from sys import stdin


def readB(b):
    l = stdin.readline()
    if l == '':
        return False

    x = []*5
    for i in range(5):
        x.append(input().split())
    b.append(x)
    return True


def test(b):
    for i in range(5):
        r = c = 0
        for j in range(5):
            r = r+int(b[i][j])
            c = c+int(b[j][i])
        if r == -5 or c == -5:
            return True
    return False


def win(b):
    for a in b:
        if test(a):
            return True
    return False
def removeWin(b):
    for a in b:
        if test(a):
            b.remove(a)


def offer(a, v):
    for b in a:
        for i in range(5):
            for j in range(5):
                if b[i][j] == v:
                    b[i][j] = -1


def calcWin(b):
    c = 0
    for a in b:
        for i in range(5):
            for j in range(5):
                if a[i][j] != -1:
                    c = c + int(a[i][j])
    return c


n = input().split(",")

b = []

while readB(b):
    continue


v = 0
while not win(b) or len(b)>1:
    removeWin(b)
    v = n[0]
    n = n[1:]
    offer(b, v)
print(calcWin(b)*int(v))
