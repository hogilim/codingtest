def dfs(answer, arr, tmp, m):
    if len(list(tmp.split())) == m:
        answer.add(tmp)
        return
    else:
        for i in range(len(arr)):
            dfs(answer, arr, tmp+" "+str(arr[i]), m)


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = set()
    dfs(answer, arr, "", m)
    answer = list(answer)
    for i in range(len(answer)):
        answer[i] = list(map(int,answer[i].split()))
    answer.sort()
    #print(answer)
    for i in answer:
        for j in i:
            print(j, end=" ")
        print()
