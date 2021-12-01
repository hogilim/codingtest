def solution(s):
    answer = []
    for i in s:
        if len(i) <= 3:
            answer.append(i)
        if len(i) > 3:
            tmp = list(i)
            t1 = 0  # t1으로부터 2칸과
            t2 = 0  # t2로부터 2칸을 교환 만약 t2 > t1일때
            f1 = 0
            f2 = len(tmp) - 1
            flag1 = 0
            flag2 = 0
            while f1+2 < len(tmp) and f2 > 0:
                if tmp[f1:f1 + 3] == ['1', '1', '1'] and flag1 == 0:
                    t1 = f1 + 2
                    flag1 = 1
                else:
                    f1 += 1
                if tmp[f2:f2 + 3] == ['1', '1', '0'] and flag2 == 0:
                    t2 = f2 + 2
                    flag2 = 1
                else:
                    f2 -= 1
                if t2 > t1 and flag1 == 1 and flag2 == 1:
                    print(t1, t2)
                    t = tmp[t1]
                    tmp[t1] = tmp[t2]
                    tmp[t2] = t
                    f1 = 0
                    f2 = len(tmp)
                    flag1 = 0
                    flag2 = 0
            answer.append("".join(tmp))
    return answer


if __name__ == "__main__":
    print(solution(["111000000110","1110","100111100","0111111010"]))
