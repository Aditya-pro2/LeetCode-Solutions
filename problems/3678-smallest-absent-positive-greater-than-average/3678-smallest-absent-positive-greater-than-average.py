class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg, c = sum(nums) / len(nums), 1
        while True:
            if c > avg and c not in nums:
                return c
            c += 1