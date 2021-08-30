from sys import stdin
l = list(stdin.readline())
if l[-1] == '\n':
    l.pop()
ll = len(l)
r = list()
rl = len(r)
n = int(stdin.readline())

for i in range(n):
    o = list(stdin.readline().split())
    if o[0] == 'L':
        if ll > 0:
            r.append(l.pop())
            ll -= 1
            rl += 1
    if o[0] == 'D':
        if rl > 0:
            l.append(r.pop())
            ll += 1
            rl -= 1
    if o[0] == 'B':
        if ll > 0:
            l.pop()
            ll -= 1
    if o[0] == 'P':
        l.append(o[1])
        ll += 1

while rl > 0:
    t = r.pop()
    if t != '\n':
        l.append(t)
    rl -= 1

print("".join(l))