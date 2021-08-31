n = int(input())         #bottom-up
l = list(map(int, input().split()))

dp = [1]*(n)
dp[0] = 1
for i in range(0, n):
    for j in range(0, i):
        if l[i] > l[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j]+1

print(max(dp))

