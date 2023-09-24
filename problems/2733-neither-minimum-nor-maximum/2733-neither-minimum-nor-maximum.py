class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        for i in nums:
            if i not in [max(nums), min(nums)]:
                return i
        return -1