import heapq
class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1)]
        heap = [(1, 0, 0, 1)]
        visited = dict() 
        while heap:
            cost, i, j, time = heapq.heappop(heap)
            if i == m - 1 and j == n - 1:
                return cost
            key = (i, j, time % 2)
            if key in visited and visited[key] <= cost:
                continue
            visited[key] = cost
            if time % 2 == 1:
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        new_cost = cost + (ni + 1) * (nj + 1)
                        heapq.heappush(heap, (new_cost, ni, nj, time + 1))
            else:
                new_cost = cost + waitCost[i][j]
                heapq.heappush(heap, (new_cost, i, j, time + 1))
        return -1