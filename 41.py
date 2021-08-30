from collections import deque
ans = deque()
n = int(input())
count = 0
ss = 0
c = 0
s = 1
e = int(n/2)+1
while s <= e:
    c += 1
    ans.append(s)
    ss+=s
    print(ans)
    while ss > n:
        c+=1
        ss-=ans.popleft()
        print(ans)
    if ss == n:
        count += 1
        for i in range(len(ans)-1):
            print(ans[i], end="")
            print(' + ', end="")
        print(ans[-1], "=", n)
    s += 1
print(count)
print(c)
