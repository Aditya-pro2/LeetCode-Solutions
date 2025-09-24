class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        l, s = set(), nums[0]
        l.add(s)
        for i in range(1, len(nums) - 1):
            s += (nums[i + 1] - nums[i - 1])
            n = len(l)
            l.add(s)
            if n == len(l):
                return True
        return False