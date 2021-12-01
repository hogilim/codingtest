jobs = list(map(int, input().split()))
numOfMach = int(input())
mach = []
time = []

print("Jobs =", jobs)
print("# of Jobs =", len(jobs), ", # of Machines =", numOfMach)
print()

for i in range(numOfMach):
    mach.append([])
    time.append(0)

jobs.sort()
while len(jobs) > 0:
    minimum = min(time)
    for i in range(numOfMach):
        if time[i] == minimum:
            temp = jobs.pop()
            time[i] += temp
            mach[i].append(temp)


for i in range(numOfMach):
    print(" Mach", i+1, "Time =", time[i], mach[i])
print(">> Final Completion Time (C.T.) =", max(time))
