import sys

value={"=":-2, "-":-1, "0":0, "1":1,"2":2}
rep = [('0',0), ('1',0), ('2',0), ('=',1), ('-',1), ('0',1)]

def f(n):
    return sum(value[v]*5**idx for idx,v in enumerate(n[::-1]))
def to(k):
    resp = ""
    rem = 0
    while k:
        c,rem = rep[k%5+rem]
        resp = c + resp
        k=k//5
    return resp
print(to(sum([f(n.strip()) for n in sys.stdin])))