import sys
from math import inf, prod

prints = False

class Monkey:
    def __init__(self, l):
        self.id = l[0][-2]
        self.items = [ int(k.strip()) for k in l[1].split(":")[1].split(",")]
        self.op, factor = l[2].split(" ")[-2:]
        self.factor = int(factor) if factor != "old" else inf
        self.div = int(l[3].split(" ")[-1])
        self.t = int(l[4].split(" ")[-1])
        self.f = int(l[5].split(" ")[-1])
        self.c = 0
    def process(self, mk):
        if prints:
            print("Monkey", self.id)
        while len(self.items)>0:
            self.c=self.c+1
            i = self.items.pop(0)
            n = i if self.factor == inf else self.factor

            if prints:
                print("Olhando para o ", i, self.op, n, end="")
            if(self.op == "*"):
                i = i * n
            else:
                i = i + n
            i = i//3
            if prints:
                print("=", i, " ", i,"%", self.div, " ", i%self.div==0)
            if i % self.div == 0:
                mk[self.t].items.append(i)
                if prints:
                    print("mandou para o ", self.t)
            else:
                mk[self.f].items.append(i)
                if prints:
                    print("mandou para o ", self.f)



l = [i.rstrip() for i in sys.stdin]


mk = []

i = 0
while i<len(l):
    mk.append(Monkey(l[i:i+6]))
    i=i+7

for i in range(20):
    for m in mk:
        m.process(mk)

resp = [m.c for m in mk]
resp.sort()
resp = prod(resp[-2:])
print(resp)