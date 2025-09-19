class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        maxSoFar = res = -inf
        for n in nums:
            if n > 0 and -n in s and n > maxSoFar:
                maxSoFar = n
                res = n
        return res if res != -inf else -1