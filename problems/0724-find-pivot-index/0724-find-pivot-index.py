class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s, ls = sum(nums), 0
        for i, j in enumerate(nums):
            rs = s - ls - j
            if ls == rs:
                return i
            ls += j
        return -1