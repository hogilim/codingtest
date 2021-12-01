# 1. 문제 조건에 나오는 리스트 생성
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']

# 2. 힌트에 나온 대로 비어있는 리스트 생성
new_s_list = []

# 3. s_list 의 원소를 하나하나 꺼내어 확인
for i in s_list:
    # 4. s_list 의 원소가 new_s_list 에 있는지 in 으로 확인 없으면 삽입
    if i not in new_s_list:
        new_s_list.append(i)

print(new_s_list)