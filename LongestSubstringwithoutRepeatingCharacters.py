from collections import deque

dq = deque()
d = {}
s = input()
for i in s:
    d[i] = 0

i = 0
ml = 0
length = 0
while i < len(s):
    dq.append(s[i])
    d[s[i]] += 1
    length += 1
    while d[s[i]] == 2:
        d[dq.popleft()] -= 1
        length -= 1
    if length > ml:
        ml = length
    i += 1

print(ml)





