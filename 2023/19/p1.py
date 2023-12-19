import sys
from collections import deque
import json

def parse(line):
    pkg = {}
    for x in line.strip()[1:-1].split(","):
        n, v=x.split("=")
        pkg[n]=int(v)
    return pkg
def evaluate(rule, pkg):
    for r in rule:
        if len(r) == 1:
            return r[0]
        r,dst = r
        item = r[0]
        op = r[1]
        threshold = int(r[2:])
        value = pkg[item]
        if op == '<' and value<threshold:
            return dst
        if op == '>' and value>threshold:
            return dst


def proc(rules, pkg):
    s = 'in'
    while s != 'A' and s!='R':
        s = evaluate(rules[s], pkg)
    return 0 if s=='R' else sum(pkg.values())


rules={}
for l in sys.stdin:
    if len(l.strip()) == 0:
        break
    name, rule = l.split("{")
    rule = rule.strip()[:-1].split(",")
    rule = [r.split(":") for r in rule]
    rules[name]=rule

total = 0
for l in sys.stdin:
    pkg = parse(l)
    total += proc(rules, pkg)
print(total)
