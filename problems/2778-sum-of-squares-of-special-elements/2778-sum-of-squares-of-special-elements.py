class Solution:
    def sumOfSquares(self, x: List[int]) -> int:
        n, c = len(x), 0
        for i in range(n):
            if n % (i + 1) == 0:
                c += (x[i] ** 2)
        return c