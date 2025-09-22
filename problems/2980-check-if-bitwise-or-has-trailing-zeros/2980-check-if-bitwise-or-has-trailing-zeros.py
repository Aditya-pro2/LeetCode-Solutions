class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        c = 0
        for i in nums:
            if i & 1 == 0:
                c += 1
                if c == 2:
                    return True
        return False