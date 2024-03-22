class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        a = 0
        for x in nums:
            for y in nums:
                if abs(x - y) <= min(x, y):
                    a = max(a, x ^ y)
        return a