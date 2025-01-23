class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        row = [0] * r
        col = [0] * c

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1

        cnt = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and (row[i] > 1 or col[j] > 1):
                    cnt += 1

        return cnt