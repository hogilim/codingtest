def solution(people, limit):
    answer = 0
    f = 0
    e = len(people) - 1
    people.sort()

    while f <= e:
        if people[f] + people[e] > limit:
            answer += 1
            e -= 1
        else:
            answer += 1
            f += 1
            e -= 1
    return answer


if __name__ == "__main__":
    print(solution([70, 50, 80, 50], 100))