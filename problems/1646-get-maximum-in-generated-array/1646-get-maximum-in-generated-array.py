class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = [0] * 101
        if n:
            dp[1] = 1
        for i in range(1, n + 1):
            if 2 * i <= n:
                dp[2 * i] = dp[i]
            if 2 * i + 1 <= n:
                dp[2 * i + 1] = dp[i] + (dp[i + 1] if i + 1 < n else 0)
        return max(dp)