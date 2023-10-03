class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        s = n = i = 0
        nums.sort()
        while i < len(nums):
            n = nums.count(nums[i])
            x = (n * (n - 1)) // 2
            s, i = s + x, i + n
        return s