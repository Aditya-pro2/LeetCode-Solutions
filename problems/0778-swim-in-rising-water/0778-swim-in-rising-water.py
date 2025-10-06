class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]
        time = 0
        while heap:
            t, i, j = heapq.heappop(heap)
            if visited[i][j]:
                continue
            visited[i][j] = True
            time = max(time, t)
            if i == n - 1 and j == n - 1:
                return time
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                    heapq.heappush(heap, (grid[ni][nj], ni, nj))
        return time