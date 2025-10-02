class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        l = []
        nums.sort()
        while len(nums) > 1: 
            l.append((nums[0] + nums[-1]) / 2)
            nums.pop(0)
            nums.pop(-1)
        return len(set(l))