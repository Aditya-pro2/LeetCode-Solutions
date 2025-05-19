class Solution:
    def triangleType(self, nums: List[int]) -> str:
        x = set(nums)
        if 2 * max(nums) >= sum(nums):
            return "none"
        if len(x) == 1:
            return "equilateral"
        if len(x) == 2:
            return "isosceles"
        return "scalene"