import sys

def find(v,i, a):
    print("find", v,i)
    for j in range(1,i,2):
        if a[j]>=v:
            print("return if", j, a[j])
            return j
    print("return f", i)
    return i
    
#print(fat)

a = [l.strip() for l in sys.stdin][0]
disk = []

for i in range(len(a)):
    x = int(a[i])
    if i%2==0:
        disk.append((i//2, x))
    else:
        disk.append((-1, x))
#print(disk)
i = len(disk)-1
while i>0:
    v,s = disk[i]
    if v==-1:
        #empty space
        i-=1
        continue
    ni = -1
    for j in range(i):
        nv,ns = disk[j]
        if nv==-1 and ns>=s:
            ni = j
            break
    if ni==-1:
        i-=1
        continue
    _,ss = disk[ni]
    disk = disk[:ni]+[(v,s), (-1, ss-s)]+disk[ni+1:i]+[(-1,s)]+disk[i+1:]
#print(disk)
sum = 0
block = 0
for i in disk:
    v,s = i
    if v ==-1:
        block+=s
        continue
    for j in range(s):
        sum+= block*v
        block+=1
print(sum)
