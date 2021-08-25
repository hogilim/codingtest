"""
1~9 9 9 * 10 0

10 ~ 99 90 9 * 10 1

100 ~ 999 900

1000 9999 9000
"""

n = input()
ans = 0
t = 1
for i in range(len(n)-1):
    ans += (9*t)*(i+1)
    t *= 10

ans += (int(n)-t+1) * len(n)
print(ans)