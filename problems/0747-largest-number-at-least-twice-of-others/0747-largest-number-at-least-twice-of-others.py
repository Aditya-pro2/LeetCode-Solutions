class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        x = nums.index(max(nums))
        nums.sort(reverse = True)
        return x if nums[0] >= (2 * nums[1]) else -1