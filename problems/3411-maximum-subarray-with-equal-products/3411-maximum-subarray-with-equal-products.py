from math import gcd
class Solution:
    def maxLength(self, a: List[int]) -> int:
        def lcm(a, b):
            return a * b // gcd(a, b)
        n, m = len(a), 0
        for i in range(n):
            p, cg, cl = 1, a[i], a[i]
            for j in range(i, n):
                p *= a[j]
                cg = gcd(cg, a[j])
                cl = lcm(cl, a[j])
                if p == cg * cl:
                    m = max(m, j - i + 1)
        return m