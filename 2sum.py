class Solution:
    def twoSum(self, nums, target):
        d = []
        for i in range(len(nums)):
            d.append([nums[i], i])
        d.sort()
        b = 0
        e = len(d) - 1
        while b < e:
            if d[b][0] + d[e][0] < target:
                print(b, e)
                b += 1
            elif d[b][0] + d[e][0] > target:
                e -= 1
            else:
                return [d[b][1], d[e][1]]


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([3,2,4], 6))