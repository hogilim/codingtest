import math


def solution(brown, yellow):
    h = 0
    v = 0
    answer = []
    for v in range(1, int(math.sqrt(yellow)+1)):
        if yellow % v == 0:
            h = yellow // v
            if brown == 2*(h+v) + 4:
                answer.append(h+2)
                answer.append(v+2)
                break
    return answer


if __name__ == "__main__":
    print(solution(10, 2))
