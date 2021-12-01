def solution(n, left, right):
    e = [i for i in range(1, n+1)]
    answer = []
    for i in range(left // n, right // n+1):
        f = [i + 1] * (i + 1)
        answer.extend(f)
        answer.extend(e[i + 1:])
    answer = answer[left % n:right - (left//n)*n + 1]
    return answer


if __name__ == "__main__":
    print(solution(3, 2, 5))
    print(solution(4,7,14))

