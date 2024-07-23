class Solution:
    def maximumProduct(self, n: List[int]) -> int:
        n.sort()
        return max(n[-1] * n[-2] * n[-3], n[-1] * n[0] * n[1])