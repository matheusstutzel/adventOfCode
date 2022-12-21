import sys

class Monkey:
    def __init__(self, exp):
        split = exp.split(" ") 
        if len(split)==1:
            self.a, self.op, self.b = None, None, None
            self.value = int(exp)
        else:
            self.a, self.op, self.b = split
            self.value = None
    def solve(self, monkeys):
        if not self.value:
            a = monkeys[self.a].solve(monkeys)
            b = monkeys[self.b].solve(monkeys)
            op = self.op

            if op == '+':
                self.value = a+b
            elif op == '-':
                self.value = a-b
            elif op == '*':
                self.value = a*b
            elif op == '/':
                self.value = a/b
            else:
                raise RuntimeError("WHAT" + str(op))
        return self.value
        
def convert(l):
    id, exp = l.strip().split(":")
    return id, Monkey(exp.strip())

monkeys = {}
for l in sys.stdin:
    id, monkey = convert(l)
    monkeys[id]=monkey

print(monkeys["root"].solve(monkeys))
'''
for id in monkeys:
    m = monkeys[id]
    print(id, m.a, m.op, m.b, m.value)
'''