class Solution:
    def countElements(self, nums: List[int]) -> int:
        a, b = min(nums), max(nums)
        return sum(1 for i in nums if a < i < b)