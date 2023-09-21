class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(len(nums)):
            a.append(abs(sum(nums[:i]) - sum(nums[(i + 1): ])))
        return a