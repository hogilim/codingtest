"""import heapq

def solution(n, times):
    tmp = []  # [끝나는 시간 시작시간 걸리는시간]
    # 끝나는 시간 = 시작시간 + 걸리는시간이 가장 작은 곳에 사람 들어감 : 시작시간 = 끝나는시간
    for i in times:
        tmp.append([i, 0, i])

    while n > 0:
        heapq.heapify(tmp)
        tmp[0][1] = tmp[0][0]
        tmp[0][0] = tmp[0][1] + tmp[0][2]
        n -= 1

    tmp.sort(key=lambda x: x[1])
    answer = tmp[-1][1]
    return answer

if __name__ == "__main__":
    print(solution(6, [7, 10]))

# 시간초과!
"""

# 시간으로 접근할 것
def solution(n, times):
    answer = 0
    s, e = 1, n*max(times) # 걸리는 시간의 최소값 최대값
    while s <= e:
        m = (s+e)//2
        done = sum(m//time for time in times)

        if done >= n:
            answer = m
            e = m - 1
        elif done < n:
            s = m + 1

    return answer

if __name__ == "__main__":
    print(solution(6, [7, 10]))
