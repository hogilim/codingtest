dp = [0]*46
dp[1] = 1
dp[2] = 2

n = int(input())

for i in range(3,n+2):
    dp[i] = dp[i-1]+dp[i-2]

print(dp)
print(dp[n+1])
