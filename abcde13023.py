def dfs(r, t, answer):
    if len(t) == 5 or answer == 1:
        answer = 1
        return answer
    for i in r:
        if i in t:
            continue
        else:
            t.append(i)
            answer = dfs(r, t, answer)
            t.pop()
    return answer


if __name__ == "__main__":
    n, m = map(int, input().split())
    r = []
    for i in range(n):
        r.append([])
    for i in range(m):
        m1, m2 = map(int, input().split())
        r[m1].append(m2)
        r[m2].append(m1)
    print(r)
    print(dfs(r, [], 0))
