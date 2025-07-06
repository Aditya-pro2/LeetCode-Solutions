class Solution:
    def minTime(self, n: int, e: List[List[int]], k: int) -> int:
        if not e:
            return 0 if k <= n else -1
        class UnionFind:
            def __init__(self, s):
                self.p = list(range(s))
                self.rk = [0] * s
                self.c = s
            def find(self, x):
                if self.p[x] != x:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]
            def union(self, x, y):
                xr, yr = self.find(x), self.find(y)
                if xr == yr:
                    return False
                if self.rk[xr] < self.rk[yr]:
                    self.p[xr] = yr
                elif self.rk[xr] > self.rk[yr]:
                    self.p[yr] = xr
                else:
                    self.p[yr] = xr
                    self.rk[xr] += 1
                self.c -= 1
                return True
        t = sorted(set(i for _, __, i in e))
        def fun(x):
            u = UnionFind(n)
            for i, j, k in e:
                if k > x:
                    u.union(i, j)
            return u.c
        l, r = 0, max(i for _, __, i in e)
        ans = r
        while l <= r:
            m = (l + r) // 2
            com = fun(m)
            if com >= k:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans