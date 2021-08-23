def solution(routes):
    routes.sort(key=lambda x: x[1])
    print(routes)
    cam = 1
    tmp = routes[0][1]
    for i in routes:
        if i[0] <= tmp and tmp <= i[1]:
            continue
        else:
            tmp = i[1]
            cam += 1
    return cam


if __name__ == "__main__":
    print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))