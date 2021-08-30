from collections import deque
ans = {}
c = 0

def solution(s):
    ss = []
    for i in s:
        ss.append([i,0])
    for i in range(len(s)):
        tmp = ""
        dfs(ss, tmp, i+1, 0)


def dfs(ss, tmp, n, l):
    global c
    c+=1
    if n == l:
        ans[tmp] = 0
        return
    else:
        for i in range(len(ss)):
            if ss[i][1] == 0:
                ss[i][1] = 1
                dfs(ss, tmp+ss[i][0], n, l+1)
                ss[i][1] = 0


if __name__ == "__main__":
    s = input()
    solution(s)
    count = 0
    for i in ans:
        count +=1
    print(count)

