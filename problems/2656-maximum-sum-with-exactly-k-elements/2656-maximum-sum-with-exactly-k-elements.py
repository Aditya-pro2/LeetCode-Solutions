class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        return (nums[-1] * k) + ((k * (k - 1)) // 2)