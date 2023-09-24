class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m, n, s = len(grid), len(grid[0]), 0
        for i in range(n):
            c = 0
            for i in range(m):
                k = max(grid[i])
                grid[i][grid[i].index(k)] = 0
                if c < k:
                    c = k
            s += c
        return s