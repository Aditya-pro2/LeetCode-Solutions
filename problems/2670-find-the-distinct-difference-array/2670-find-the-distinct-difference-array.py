class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        diff, n = [], len(nums)
        for i in range(n):
            diff.append(len(set(nums[:i+1])) - len(set(nums[i+1:])))
        return diff