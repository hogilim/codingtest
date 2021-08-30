n = int(input())
f = list(map(int, input().split()))
r = list(map(int, input().split()))
count = 0
for i in r:
    print(i)
    tmp = f[:]
    for j in range(len(tmp)):
        if i < tmp[j]:
            tmp[j] = i
    count += sum(tmp)
    print(tmp)

print(count)