class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return 1 if nums.count(nums[0]) < len(nums) else 0