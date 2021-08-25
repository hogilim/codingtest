# 3초 정렬
n = int(input())
l = list(map(int, input().split()))
s = sorted(l)
i = n - 1
count = 0
change = []
while i > 0:
    if l[i-1] > l[i]:
       count += 1
       l[i-1] = l[i]
       change.append([i, l[i]])
    i -= 1

print(l)

if count <= 3:
    print("YES")
    print(count)
    for i in change:
        print(i[0], i[1])
else:
    print("NO")
