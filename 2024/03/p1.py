import re
import sys

reg = "mul\(([0-9]{1,3}),([0-9]{1,3})\)"

sum = 0 
for line in sys.stdin:
    for x,y in  re.findall(reg, line):
        sum += int(x)*int(y)
print(sum)
