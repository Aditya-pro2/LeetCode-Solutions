class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            c += (len(str(i)) % 2 == 0)
        return c