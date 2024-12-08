import sys

def findInvalid(nums,i, rule):
    v = nums[i]
    if v not in rule:
        return -1
    for j in range(i):
        if nums[j] in rule[v]:
            return j
    return -1

def mySort(nums, rule, step=0):
    p=-1
    for i in range(len(nums)):
        p = findInvalid(nums, i, rule)
        if(p!=-1):
            nums = nums[:p]+[nums[i]]+nums[p:i]+nums[i+1:]
            break
    if(p==-1):
        return nums
    return mySort(nums, rule, step+1)
            
    
    

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

print(rule)

sum = 0 
for l in sys.stdin:    
    nums= [int(x) for x in l.strip().split(",")]
    points = process(nums, rule)
    if points != 0:
        #already valid
        continue
    nums = mySort(nums, rule)
    sum+=process(nums, rule)
print(sum)
