n = int(input())
min_num = [i for i in range(n+1)]
max_num = [i for i in range(9,8-n,-1)]
s = list(input().split())

for j in range(len(s)):
    for i in range(len(s)):
        if s[i] == ">":
            if min_num[i] < min_num[i+1]:
                min_num[i], min_num[i+1] = min_num[i+1], min_num[i]
            if max_num[i] < max_num[i+1]:
                max_num[i], max_num[i+1] = max_num[i+1], max_num[i]
        else:
            if min_num[i] > min_num[i+1]:
                min_num[i], min_num[i+1] = min_num[i+1], min_num[i]
            if max_num[i] > max_num[i+1]:
                max_num[i], max_num[i+1] = max_num[i+1], max_num[i]

max_num = map(str, max_num)
min_num = map(str, min_num)
print("".join(max_num))
print("".join(min_num))
