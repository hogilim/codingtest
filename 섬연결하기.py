def getRoot(u, k):
    if u[k] == k:
        return k
    else:
        return getRoot(u, u[k])


def union(u, s, e):
    a = getRoot(u, s)
    b = getRoot(u, e)
    if a > b:
        u[s] = b
    else:
        u[e] = a
    print(u)

def solution(n, costs):
    answer = 0
    for i in costs:
        if i[0] > i[1]:
            tmp = i[0]
            i[0] = i[1]
            i[1] = tmp
    costs.sort(key=lambda x: x[2])
    u = [i for i in range(n)]
    road = []
    for i in costs:
        if u[i[0]] == u[i[1]]:
            continue
        else:
            union(u, i[0], i[1])
            road.append(i)
    for i in road:
        answer += i[2]
    print(costs)
    print(u)
    print(road)
    return answer


if __name__ == "__main__":
    a = [[0,6,12],[3,6,13],[0,4,17],[2,4,20],[1,3,24],[0,3,28],[2,5,37],[4,5,45],[1,4,62],[0,1,67],[4,6,73]]
    b = [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]
    print(solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]))
