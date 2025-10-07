class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        x, c, n = -1, 0, len(nums)
        for i in range(n - 1):
            if nums[i] >= nums[i + 1]:
                x = i
                c += 1
        if c == 0:
            return True
        if c == 1:
            if x == 0 or x == n - 2:
                return True
            if nums[x - 1] < nums[x + 1] or (x + 2 < n and nums[x] < nums[x + 2]):
                return True
        return False