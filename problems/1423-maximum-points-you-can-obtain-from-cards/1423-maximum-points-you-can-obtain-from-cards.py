class Solution:
    def maxScore(self, a: List[int], k: int) -> int:
        sl, sr = sum(a[:k]), 0
        x = sl
        for i in range(k):
            sl -= a[k - i - 1]
            sr += a[len(a) - i - 1]
            x = max(x, sl + sr)
        return x