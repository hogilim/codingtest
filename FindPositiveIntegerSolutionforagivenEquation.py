class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int):
        c = customfunction
        answer = []
        for i in range(1, 1001):
            if c.f(i, 1) > z:
                break
            for j in range(1, 1001):
                if c.f(i, j) > z:
                    break
                if z == c.f(i, j):
                    answer.append([i, j])
        return answer
