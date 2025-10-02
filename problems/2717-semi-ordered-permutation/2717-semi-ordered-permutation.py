class Solution:
    def semiOrderedPermutation(self, nums: list[int]) -> int:
        n = len(nums)
        first = nums.index(1)
        last = nums.index(n)
        return first + (n - 1 - last) if first <= last else first + (n - 1 - last) - 1