from sys import stdin
ab = list(map(int, stdin.readlines().split()))
i = 0
while i < len(ab)-1:
    print(ab[i]+ab[i+1])
    i+=2
