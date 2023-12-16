import sys

lines = [l.strip().split(",") for l in sys.stdin]


total = 0
for p in lines[0]:
    local = 0
    for c in p:
        local = ((local + ord(c))*17)%256
    total = total + local
print(total)