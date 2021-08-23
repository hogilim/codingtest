import random
import time
te = {1: "종혁", 2: "경민", 3: "보경", 4: "호기"}
c = [0]*5
t = []

for i in range(len(te)):
    while 1:
        a = random.randrange(1, 5)
        if c[a] == 0 and i+1 != a:
            c[a] = 1
            t.append(a)
            break

i = 0
while i < 4:
    tmp = input("enter")
    print(te[i+1], "쌤의 마니또는", te[t[i]])
    time.sleep(1)
    for j in range(10000):
        print()
    i += 1
