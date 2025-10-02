class Solution:
    def minimumRightShifts(self, nums: list[int]) -> int:
        valid = sorted(nums)
        if nums == valid:
            return 0
        n = len(nums)
        idx = nums.index(min(nums))
        swap = [0] * n
        for i in range(n):
            swap[i] = nums[(i + idx) % n]
        return n - idx if swap == valid else -1