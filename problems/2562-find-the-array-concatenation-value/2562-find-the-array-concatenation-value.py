class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        N = len(nums)
        half_N = N // 2
        ans = 0
        if N % 2 == 1:
            ans = nums[half_N]
        for i in range(half_N):
            ans += int(str(nums[i]) + str(nums[N - 1 - i]))
        return ans