import sys



def test(design, cache={}):
    if design in cache:
        return cache[design]

    if len(design)==0:
        cache[design]=True
        return True
    for o in options:
        if design.startswith(o) and test(design[len(o):], cache):
            cache[design]=True
            return True
    cache[design]=False
    return False


options = [l.strip() for l in input().strip().split(",")]
input()

query = [l.strip() for l in sys.stdin]

result = 0 
for q in query:
    if test(q):
        result+=1
print(result)
