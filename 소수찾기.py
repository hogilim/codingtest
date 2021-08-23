e = [1 for i in range(10000001)]
e[0] = 0
e[1] = 0
for i in range(2, 1001):
    j = i
    if e[i] == 0:
        continue
    k = 2
    while k*i <= 10000000:
        e[i*k] = 0
        k += 1


def dfs(c, num, s, n):
    if s != "":
        c.add(int(s))
    if len(s) > n:
        return
    else:
        for i in num:
            if i[1] == 0:
                i[1] = 1
                dfs(c, num, s+i[0], n)
                i[1] = 0


def solution(numbers):
    c = set()
    answer = 0
    num = []
    for i in numbers:
        num.append([i, 0])
    dfs(c, num, "", len(numbers))
    for i in c:
        if e[i] == 1:
            answer += 1
    return answer


if __name__ == "__main__":
    print(solution("17"))