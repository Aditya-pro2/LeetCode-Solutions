class Solution:
    def flipAndInvertImage(self, x: List[List[int]]) -> List[List[int]]:
        n = len(x)
        l = n // 2
        if n % 2 != 0:
            l += 1
        for i in range(n):
            for j in range(l):
                t = x[i][j]
                x[i][j] = x[i][n - j - 1]
                x[i][n - j - 1] = t
        for i in range(n):
            for j in range(n):
                x[i][j] = 1 - x[i][j]
        return x