class Solution:
    def maxDivScore(self, nums, divisors):
        m = b = None
        for i, d in enumerate(divisors):
            x = 0
            for n in nums:
                if (n % d == 0):
                    x += 1
            if m is None or x >= m:
                b = min(b, d) if x == m else d
                m = x
        return b