class Solution:
    def arraySign(self, nums: List[int]) -> int:
        return 0 if 0 in nums else 1 if sum(n < 0 for n in nums) % 2 == 0 else -1