class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = float("inf")
        for i in range(n):
            orr = nums[i]
            for j in range(i, n):
                orr |= nums[j]
                if orr >= k:
                    m = min(m, j - i + 1)
                    break
        if m == float("inf"):
            return -1
        return m