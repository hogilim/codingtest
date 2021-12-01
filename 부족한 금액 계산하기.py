def solution(price, money, count):
    s = 0
    answer = 0
    for i in range(count+1):
        s += i
    p = s * price
    if p>money:
        answer = p-money
    return answer


if __name__ == "__main__":
    print(solution(3,20,4,10))