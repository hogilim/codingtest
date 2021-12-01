f = open("/Users/limhogi/Downloads/mj10-1000fm1.txt", "r")
a = []
while True:
    line = f.readline()
    if not line:
        break
    a.extend(list(line.split()))
print(a)

a = [1,3,2]
print(max(a), min(a))