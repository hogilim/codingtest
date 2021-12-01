#
# def get_multiples(num):
#     multiple = []
#     i = 1
#     while num * i <= 1000:
#         multiple.append(num * i)
#         i += 1
#     return multiple
#
#
# a = int(input("첫번째 숫자: "))
# b = int(input("두번째 숫자: "))
#
# a_mul = get_multiples(a)
# b_mul = get_multiples(b)
#
# gcf = 0
#
# for i in a_mul:
#     if i in b_mul:
#         gcf = i
#         break
#
# ab_mul = get_multiples(gcf)
#
# print(a, "의 배수 =", a_mul)
# print(b, "의 배수 =", b_mul)
# print("공배수 = ", ab_mul)
# print("최소공배수", gcf)


num1, num2 = map(int, input().split())

def small(l):


def get_multiples(num1, num2):      # 함수 구현!! 함수 코드는 함수가 사용될 때 실행된다.
    muls = []
    num1_muls = []
    num2_muls = []
    for i in range(1, 1001):
        if i % num1 == 0 and i % num2 == 0:
            muls.append(i)
        elif i % num1 == 0:
            num1_muls.append(i)
        elif i % num2 == 0:
            num2_muls.append(i)

    return muls, num1_muls, num2_muls  #   밖에서 값을 사용하기 위해 함수 밖으로 값 리턴


m, m1, m2 = get_multiples(num1,num2)    # 함수 사용 !! 위에 구현된 함수가 동작한다. 리턴되는 값 받아주기

print(m,m1,m2, min(m), sep='\n')

