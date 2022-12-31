import sys

def calc(l,w,h):
    a = l*w
    b = w*h
    c = h*l
    return 2*a+2*b+2*c + min(a,min(b,c))

l = sum([calc(*([ int(k) for k in l.strip().split("x")])) for l in sys.stdin])
print(l)