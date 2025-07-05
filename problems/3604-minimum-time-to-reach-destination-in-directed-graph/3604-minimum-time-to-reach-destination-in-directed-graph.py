import heapq
from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, start, end in edges:
            graph[u].append((v, start, end))
        heap = [(0, 0)]
        visited = [float('inf')] * n
        visited[0] = 0
        while heap:
            time, node = heapq.heappop(heap)
            if node == n - 1:
                return time
            if time + 1 < visited[node]:
                visited[node] = time + 1
                heapq.heappush(heap, (time + 1, node))
            for nei, start, end in graph[node]:
                if start <= time <= end:
                    if time + 1 < visited[nei]:
                        visited[nei] = time + 1
                        heapq.heappush(heap, (time + 1, nei))
                elif time < start:
                    if start + 1 < visited[nei]:
                        visited[nei] = start + 1
                        heapq.heappush(heap, (start + 1, nei))
        return -1