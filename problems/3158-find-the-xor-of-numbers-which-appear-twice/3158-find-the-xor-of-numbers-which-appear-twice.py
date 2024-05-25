class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        x = 0
        for i in set(nums):
            if nums.count(i) == 2:
                x = x ^ i
        return x