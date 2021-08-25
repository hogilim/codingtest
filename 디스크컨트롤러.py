import heapq as hq
from collections import deque


def solution(jobs):
    jobs.sort()
    t = 0
    answer = 0
    wait = deque(jobs)
    done = deque()
    done.append(wait.popleft())
    time = done[-1][0] + done[-1][1]
    answer += done[-1][1]
    tmp = []
    while len(wait) > 0:
        while len(wait) > 0 and wait[0][0] < time:
            t = wait.popleft()
            hq.heappush(tmp, [t[1], t[0]])
        if len(tmp) == 0:
            t = wait.popleft()
            done.append([t[1], t[0]])
            time = t[1] + t[0]
            answer += t[1]
            continue

        done.append(hq.heappop(tmp))
        time += done[-1][0]
        answer += time - done[-1][1]
    while len(tmp) > 0:
        done.append(hq.heappop(tmp))
        time += done[-1][0]
        answer += time - done[-1][1]
    print(done)
    return answer//len(jobs)


if __name__ == "__main__":
    print(solution([[0,1],[0,2],[2,1]]))

