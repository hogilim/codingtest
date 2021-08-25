import time
n = int(input())
task = []
for i in range(n):
    task.append(int(input()))
k = int(input())
minn = 10000
nz = n
while k >= nz:
    print(k, nz, task)
    for i in task:
        if i != 0 and i < minn:
            minn = i

    if minn * nz < k:
        for i in range(n):
            if task[i] != 0:
                task[i] -= minn
                k -= minn
            if task[i] == 0:
                nz -= 1
        print(k)

    else:
        for i in range(n):
            if task[i] != 0:
                task[i] -= k//nz
                k -= k//nz
            if task[i] == 0:
                nz -= 1
        print(k)

i = 0
while k >= 0:
    if task[i] != 0:
        k -= 1
    i += 1
    if i > n:
        break
if i > n:
    print(-1)
else:
    print(i+1)
