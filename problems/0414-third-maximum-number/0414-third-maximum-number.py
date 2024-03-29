class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = sorted(list(set(nums)))
        if len(l) >= 3:
            return l[-3]
        return l[-1]