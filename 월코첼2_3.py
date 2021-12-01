from collections import deque as dq
def movex(n, m, x1, y1, qx):
    x = x1
    for q in qx:
        if q[0] == 2:
            x -= q[1]
            if x < 0:
                x = 0
        if q[0] == 3:
            x += q[1]
            if x >= n:
                x = n-1
    return x
def movey(n, m, x1, y1, qy):
    y = y1
    for q in qy:
        if q[0] == 0:
            y -= q[1]
            if y < 0:
                y = 0
        if q[0] == 3:
            y += q[1]
            if y >= n:
                y = n-1
    return y

def solution(n, m, x, y, queries):
    answer = 0
    q = dq(queries)
    qx = []
    qy = []

    while len(q) > 0:
        if q[0][0] < 2:
            if len(qy) == 0:
                qy.append(q.popleft())
            else:
                if qy[-1][0] == q[0][0]:
                    qy[-1][1] += q[0][1]
                    q.popleft()
                else:
                    qy.append(q.popleft())
        else:
            if len(qx) == 0:
                qx.append(q.popleft())
            else:
                if qx[-1][0] == q[0][0]:
                    qx[-1][1] += q[0][1]
                    q.popleft()
                else:
                    qx.append(q.popleft())
    for i in range(n):
        for j in range(m):
            x1= movex(n, m, i, j, qx)
            if x1 != x:
                continue
            y1 = movey(n,m,i,j,qy)
            if y1 != y:
                continue
            answer += 1
    return answer


if __name__ == "__main__":
    print(solution(2,	5,	0,	1,	[[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))
