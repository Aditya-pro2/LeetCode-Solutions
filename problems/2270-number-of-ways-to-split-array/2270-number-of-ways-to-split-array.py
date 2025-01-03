class Solution:
    def waysToSplitArray(self, a: List[int]) -> int:
        s, t, c = sum(a), 0, 0
        for i in range(len(a) - 1):
            s, t = s - a[i], t + a[i]
            c += (t >= s)
        return c