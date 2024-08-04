class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s = sum(i for i in nums if i >= 1 and i <= 9)
        d = sum(i for i in nums if i >= 10)
        return s != d