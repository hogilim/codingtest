# binary search
from collections import deque
import bisect
al = []
n = int(input())
l = deque(list(map(int, input().split())))
al.append(l.popleft())
count = 1
while len(l) != 0:
    t = l.popleft()
    if al[-1] < t:
        al.append(t)
        count += 1
    else:
        al[bisect.bisect_left(al, t)] = t
    print(al)
print(len(al))