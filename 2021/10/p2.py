import sys

def process(l):
    entry = {'(':(')',1), '[':(']',2),'{':('}',3),'<':('>',4)}
    close = {')':('(',3), ']':('[',57),'}':('{',1197),'>':('<',25137)}
    stack = []
    for c in l:
        if c in entry:
            stack.append(c)
        else:
            expected, points = close.get(c)
            actual = stack.pop()
            if actual!=expected:
                return 0
    total = 0
    while stack:
        c = stack.pop()
        total = total*5 + entry.get(c)[1]    
    return total
                




l = [process(l.strip()) for l in sys.stdin]
l = list(filter(lambda x:x!=0,sorted(l)))
print(l[len(l)//2])