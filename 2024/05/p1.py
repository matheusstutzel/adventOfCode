import sys

def process(nums, rule):
    read = set()
    for n in nums:
        if n in rule and len(rule[n].intersection(read))>0:
            return 0
        read.add(n)
    return nums[len(nums)//2]


rule = {}
for l in sys.stdin:
    if len(l.strip())==0:
        break
    a,b = [int(x) for x in l.strip().split("|")]
    if a not in rule:
        rule[a]=set()
    rule[a].add(b)

sum = 0 
for l in sys.stdin:    
    nums= [int(x) for x in l.strip().split(",")]
    sum+=process(nums, rule)
print(sum)
