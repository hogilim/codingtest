import re


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s = ""
        for i in source:
            s += i
            s += '?'
        #print(s)
        p = re.compile(s)
        ans = p.findall(target)
        ans.pop()
        print(ans)
        tmp = "".join(ans)
        if tmp == target:
            return len(ans)
        else:
            return -1


if __name__ == "__main__":
    s = input()
    t = input()
    answer = Solution
    print(answer.shortestWay(Solution, s, t))
