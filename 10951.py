import sys

l = sys.stdin.readlines()
for i in l:
    try:
        a, b = map(int,i.split())
        print(a+b)
    except EOFError:
        break