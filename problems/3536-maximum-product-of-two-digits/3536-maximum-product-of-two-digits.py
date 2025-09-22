class Solution:
    def maxProduct(self, n: int) -> int:
        l = sorted(map(int, list(str(n))))
        return l[-1] * l[-2]