class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = [0] * n, [0] * n
        l[0], r[-1] = nums[0], nums[-1]
        for i in range(1, n):
            l[i] = l[i - 1] + nums[i]
        for i in range(n - 2, -1, -1):
            r[i] = r[i + 1] + nums[i]
        for i in range(len(l)):
            if l[i] == r[i]:
                return i
        return -1