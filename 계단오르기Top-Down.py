dy = [0]*46

def dfs(n):
    if dy[n] != 0:
        return dy[n]
    if n == 1:
        return n
    if n == 2:
        return n
    dy[n] = dfs(n-1) + dfs(n-2)
    return dy[n]

n = int(input())
print(dfs(n))