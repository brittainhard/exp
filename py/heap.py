import heapq
import random

def heapq_thing():
    a = [x for x in range(10)]
    random.shuffle(a)
    h = []
    for x in a:
        heapq.heappush(h, x)
    print(h, a)
    return [heapq.heappop(h) for i in range(len(h))]

print(heapq_thing())
