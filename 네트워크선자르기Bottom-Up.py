#점화식
line = [0 for i in range(46)]
line[1] = 1
line[2] = 2

n = int(input())

for i in range(3,n+1):
    line[i] = line[i-2] + line[i-1]

print(line[n])
