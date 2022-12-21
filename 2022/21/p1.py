import sys

class Monkey:
    operator = {
        "+": lambda x,y: x+y,
        "-": lambda x,y: x-y,
        "*": lambda x,y: x*y,
        "/": lambda x,y: x/y,
    }

    def __init__(self, exp):
        split = exp.strip().split(" ") 
        self.a = self.op = self.b = None
        self.value = None
        if len(split)==1:
            self.value = int(exp)
        else:
            self.a, self.op, self.b = split
    def solve(self, monkeys):
        if self.value:
            return self.value

        a = monkeys[self.a].solve(monkeys)
        b = monkeys[self.b].solve(monkeys)
        self.value = Monkey.operator[self.op](a,b)
        return self.value
        
monkeys = {}
for l in sys.stdin:
    id, exp = l.strip().split(":")
    monkeys[id]=Monkey(exp)

print(monkeys["root"].solve(monkeys))