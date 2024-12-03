import re
import sys

def calc(s):
    reg = "mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    sum = 0
    for x,y in  re.findall(reg, s):
        sum += int(x)*int(y)
    return sum


sum = 0 
line = "".join([l for l in sys.stdin])
split = line.split("don't()")
#start enabled
sum+=calc(split[0])
for t in range(1,len(split)):
    s2 = split[t].split("do()", 1)
    #discard everything before "do()"
    if len(s2)>1:
        sum+=calc(s2[1])
print(sum)
