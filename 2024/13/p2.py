import sys

def parseLine(line, div='+'):
    x,y = line.split(':')[1].strip().split(",")
    x = int(x.split(div)[1].strip())
    y = int(y.split(div)[1].strip())
    return x,y
def solve(la, lb, lp):
    xa,ya = parseLine(la)
    xb,yb = parseLine(lb)
    xp,yp = parseLine(lp, "=")
    xp+=10000000000000
    yp+=10000000000000

    # I: xa*A + xb*B = xp
    # II: ya*A + yb*B = yp II

    # III (from I): A = (xp - xb*B)/xa
    # IV (apply III on II): ya*[(xp - xb*B)/xa] + yb*B = yp 
    #    => ya*(xp-xb*B) + xa*yb*B = yp*xa
    #    => B*(xa*yb -ya*xb) = yp*xa - ya*xp
    #    => B = (yp*xa - ya*xp)/(xa*yb -ya*xb)
    # invalid if B is not int
    # apply IV on III
    # invalid if A is not int

    b =  (yp*xa - ya*xp)/(xa*yb -ya*xb)
    a = (xp - xb*b)/xa
    if int(b)-b or int(a)!=a:
        return 0
    if  a<0 or b<0:
        return 0
    return a*3 + b

tokens = 0 
prob = []
for l in sys.stdin:
    if len(l.strip()) == 0:
        tokens+=solve(*prob)
        prob = []
        continue
    prob.append(l.strip())
tokens+=solve(*prob)
print(tokens)
