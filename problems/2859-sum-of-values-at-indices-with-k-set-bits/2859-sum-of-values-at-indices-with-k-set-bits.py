class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s = 0
        for i in range(len(nums)):
            count, n = 0, i
            while (n):
                count += n & 1
                n >>= 1
            if count == k:
                s += nums[i]
        return s