class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        m, n = nums[-1], len(nums)
        for i in range(n // 2):
            x = (nums[i] + nums[n - i - 1]) / 2
            if m > x:
                m = x
        return m