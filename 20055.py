from collections import deque


class Solution:
    def __init__(self, n, k, b):
        self.z = 0
        self.n = n-1
        self.k = k
        tmp = []
        for i in b:
            tmp.append([i,0])
        self.belt = deque(tmp)

    def conveyorBelt(self):
        count = 0
        while True:
            count += 1
            self.stage1()
            self.stage2()
            self.stage3()
            if self.z >= self.k:
                return count

    def stage1(self):
        self.belt[self.n][1] = 0
        self.belt.appendleft(self.belt.pop())
        self.belt[self.n][1] = 0

    def stage2(self):
        i = self.n
        while i > 0:
            if self.belt[i-1][1] == 1 and self.belt[i][1] == 0 and self.belt[i][0] > 0:
                self.belt[i-1][1] = 0
                self.belt[i][1] = 1
                self.belt[i][0] -= 1
                if self.belt[i][0] == 0:
                    self.z += 1
            i -= 1

    def stage3(self):
        if self.belt[0][0] > 0:
            self.belt[0][1] = 1
            self.belt[0][0] -= 1
            if self.belt[0][0] == 0:
                self.z += 1


if __name__ == "__main__":
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    s = Solution(n, k, b)
    print(s.conveyorBelt())

