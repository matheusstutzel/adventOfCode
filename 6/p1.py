from sys import stdin


size = 10
c = [0 for x in range(size)]


for i in stdin.readline().split(","):
    c[int(i)] = c[int(i)]+1
print(c)

for i in range(80):
    for j in range(9):
        if j==0:
            c[9]=c[0]
            c[7]=c[7]+c[0]
        c[j]=c[j+1]
    c[9]=0
    print(i+1, c, sum(c))
print(sum(c))