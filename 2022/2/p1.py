import sys

def evaluate(a,b):
    #elf selection 
    e = ord(a[0]) - ord('A')
    #my selection
    m = ord(b[0]) - ord('X')
    # draw, win, loss
    points = [3,6,0]
    return (m+1) + points[(m-e)%3]

# total points
sum = 0

for line in sys.stdin:
    a,b = line.rstrip().split(" ")
    sum = sum + evaluate(a,b)
print(sum)

