#재귀,메모이제이션
n = int(input())
dy = [0]*(n+1)
dy[1] = 1
dy[2] = 2
def dfs(n):
    if dy[n] != 0:
        return dy[n]    # 기록된 값 나오면 리턴
    if n == 1:
        return 1
    if n == 2:
        return 2
    dy[n] = dfs(n-1) + dfs(n-2)
    return dy[n]

print(dfs(n))