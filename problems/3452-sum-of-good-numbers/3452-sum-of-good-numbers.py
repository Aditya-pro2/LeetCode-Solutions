class Solution:
    def sumOfGoodNumbers(self, nums, k):
        s, n = 0, len(nums)
        for i in range(n):
            x = True            
            if (i - k >= 0 and nums[i] <= nums[i - k]) or (i + k < n and nums[i] <= nums[i + k]):
                x = False
            if x:
                s += nums[i]
        return s