import sys

class Monkey:
    def __init__(self,exp):
        split = exp.strip().split(" ") 
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
    def solveP2(self, monkeys, expected):
        if self.value:
            return self.value
        if not self.a and not self.b:
            self.value = expected
            return expected
        try:
            selected = 1 
            result = monkeys[self.a].solve(monkeys)
        except:
            selected = 2
            result = monkeys[self.b].solve(monkeys)
        op = self.op

        if(selected == 1):
            if op == '+':
                newExpected = expected - result
            elif op == '-':
                newExpected = result - expected
            elif op == '*':
                newExpected = expected/result
            elif op == '/':
                newExpected = result/expected
            else:
                raise RuntimeError("WHAT" + str(op))
            ans = monkeys[self.b].solveP2(monkeys, newExpected)
        else:
            if op == '+':
                newExpected = expected - result
            elif op == '-':
                newExpected = result + expected
            elif op == '*':
                newExpected = expected/result
            elif op == '/':
                newExpected = expected*result
            else:
                raise RuntimeError("WHAT" + str(op))
            ans = monkeys[self.a].solveP2(monkeys, newExpected)

        return ans
    def root(self, monkeys):
        try:
            selected = 1 
            result = monkeys[self.a].solve(monkeys)
        except:
            selected = 2
            result = monkeys[self.b].solve(monkeys)

        other = self.b if selected == 1 else self.a
        return monkeys[other].solveP2(monkeys, result)

monkeys = {}
for l in sys.stdin:
    id, exp = l.strip().split(":")
    monkeys[id]=Monkey(exp)

monkeys['humn'].value = None
print(monkeys["root"].root(monkeys))

'''
for id in monkeys:
    m = monkeys[id]
    print(id, m.a, m.op, m.b, m.value)
'''