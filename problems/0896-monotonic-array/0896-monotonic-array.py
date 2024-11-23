class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        x = sorted(nums)
        return nums == x or nums == x[::-1]