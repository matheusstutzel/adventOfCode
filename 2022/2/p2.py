import sys

def evaluate(a,b):
    #elf selection 
    # 0 R, 1 P, 2 S
    e = ord(a[0]) - ord('A')
    #should 0 lose, 1 draw, 2 win
    m = ord(b[0]) - ord('X')
    
    points = [0,3,6]

    return points[m] + ((m-1 +e )%3 +1)
#  12725 

# total points
sum = 0

for line in sys.stdin:
    a,b = line.rstrip().split(" ")
    sum = sum + evaluate(a,b)
print(sum)

