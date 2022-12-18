import sys

def process(l):
    entry = {'(', '[','{','<'}
    close = {')':('(',3), ']':('[',57),'}':('{',1197),'>':('<',25137)}
    stack = []
    for c in l:
        if c in entry:
            stack.append(c)
        else:
            expected, points = close.get(c)
            actual = stack.pop()
            if actual!=expected:
                return points
    return 0
                




l = sum([process(l.strip()) for l in sys.stdin])

print(l)