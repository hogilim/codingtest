def confusingNumber(n):
    f = ['2', '3', '4', '5', '7']
    t = {'0':'0', '1':'1', '6':'9','8':'8', '9':'6'}
    s = str(n)
    for i in s:
        if i in f:
            return False
    tmp = []
    ans = ""
    for i in s:
        tmp.append(t[i])
    while(tmp):
        ans += tmp.pop()
    print(ans)
    if ans != s:
        return True
    else:
        return False


if __name__ == "__main__":
    n = int(input())
    print(confusingNumber(n))
