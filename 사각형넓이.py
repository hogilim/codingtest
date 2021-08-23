n, c = map(int, input().split())
nx = n
ny = n
for i in range(c):
    x, y = map(int, input().split())

    if nx < x or ny < y:
        continue

    rec1 = x * ny
    rec2 = y * nx
    if rec1 >= rec2:
        nx = x
    else:
        ny = y

print(nx*ny)