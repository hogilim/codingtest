n = int(input())
m = int(input())
broken = []
if m > 0:
    broken = list(input().split())

count = abs(n - 100)

for ch in range(1000001):
    f = False
    tmp = str(ch)
    for i in tmp:
        if i in broken:
            f = True
            break
    if f:
        continue
    else:
        count = min(count, abs(n-ch)+len(tmp))

print(count)