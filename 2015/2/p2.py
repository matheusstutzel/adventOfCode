import sys

def calc(l,w,h):
    x = l+w+h - max(l,w,h)
    return l*w*h + 2*x

l = sum([calc(*([ int(k) for k in l.strip().split("x")])) for l in sys.stdin])
print(l)