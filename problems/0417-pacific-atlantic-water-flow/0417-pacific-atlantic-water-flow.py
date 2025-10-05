class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j, vis):
            vis.add((i, j))
            for dx, dy in d:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    if (x, y) not in vis and heights[x][y] >= heights[i][j]:
                        dfs(x, y, vis)
        a, b = set(), set()
        for j in range(n):
            dfs(0, j, a)
        for i in range(m):
            dfs(i, 0, a)
        for j in range(n):
            dfs(m - 1, j, b)
        for i in range(m):
            dfs(i, n - 1, b)
        return list(a & b)