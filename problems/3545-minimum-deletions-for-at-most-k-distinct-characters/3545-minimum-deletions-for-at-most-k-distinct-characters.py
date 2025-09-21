class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        l = sorted(Counter(s).values())
        n = len(l)
        s = 0
        for i in range(n - k):
            s += l[i]
        return s