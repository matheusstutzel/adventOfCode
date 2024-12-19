import sys

def test(design, cache={}):
    if design in cache:
        return cache[design]

    if len(design)==0:
        cache[design]=1
        return 1
    count = 0
    for o in options:
        if design.startswith(o):
            count+= test(design[len(o):], cache)
    cache[design]=count
    return count


options = [l.strip() for l in input().strip().split(",")]
input()

query = [l.strip() for l in sys.stdin]

result = 0 
for q in query:
    result+= test(q)
print(result)
