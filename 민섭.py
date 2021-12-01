n = 0
count = 0
arr = []
while True:  # 무한루프
    n = int(input("정수를 입력하세요: "))
    if n == -99:
        break
    count += 1
    arr.append(n)

# 파이썬 리스트 (배열과 비슷한 자료구조) 를 잘 이용
print(count, "개의 유효한 정수 중", sep="") # 출력 결과 맞추기 위해 sep = ""을 통해 count와 개의 유효한 정수 붙여줌
print("가장 큰 정수:", max(arr))
print("가장 작은 정수:", min(arr))
print("평균:", sum(arr)/count)
