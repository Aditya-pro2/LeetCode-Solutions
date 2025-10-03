class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        if n == 0:
            return 0
        p, s = 0, n - 1
        while p + 1 < n and nums[p + 1] > nums[p]:
            p += 1
        if p == n - 1:
            return (n * (n + 1)) // 2
        while s > 0 and nums[s] > nums[s - 1]:
            s -= 1
        ans += (p + n - s + 2)
        i, j = 0, s
        while i <= p:
            while j < n and nums[i] >= nums[j]:
                j += 1
            ans += n - j
            i += 1
        return ans