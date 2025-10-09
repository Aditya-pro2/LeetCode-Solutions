class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        x = 0
        for i in nums:
            if i & 1 == 0:
                x |= i
        return x