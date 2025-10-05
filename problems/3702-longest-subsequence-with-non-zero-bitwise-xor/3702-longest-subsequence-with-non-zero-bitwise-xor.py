class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        s, n = 0, len(nums)
        for i in nums:
            s ^= i
        if s != 0:
            return n
        for i in nums:
            if i != 0:
                return n - 1
        return 0