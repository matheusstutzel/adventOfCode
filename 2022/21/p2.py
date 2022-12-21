import sys

class Monkey:
    operator = {
        "+": lambda x,y: x+y,
        "-": lambda x,y: x-y,
        "*": lambda x,y: x*y,
        "/": lambda x,y: x/y,
    }

    operatorA = {
        "+": lambda x,y: x-y,
        "-": lambda x,y: y-x,
        "*": lambda x,y: x/y,
        "/": lambda x,y: y/x,
        "=": lambda x,y: y
    }

    operatorB = {
        "+": lambda x,y: x-y,
        "-": lambda x,y: x+y,
        "*": lambda x,y: x/y,
        "/": lambda x,y: x*y,
        "=": lambda x,y: y
    }
    def __init__(self,exp):
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
    def solveP2(self, monkeys, expected):
        if self.value:
            return self.value
        if not self.a and not self.b:
            self.value = expected
            return expected
        try:
            operator = Monkey.operatorA
            other = self.b
            result = monkeys[self.a].solve(monkeys)
        except:
            operator = Monkey.operatorB
            other = self.a
            result = monkeys[self.b].solve(monkeys)

        expected = operator[self.op](expected,result)
        
        return monkeys[other].solveP2(monkeys, expected)

monkeys = {}
for l in sys.stdin:
    id, exp = l.strip().split(":")
    monkeys[id]=Monkey(exp)

monkeys['humn'].value = None
monkeys["root"].op = "="
print(monkeys["root"].solveP2(monkeys,0))