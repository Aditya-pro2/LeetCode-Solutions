import numpy as np
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        l = [j for i in grid for j in i]
        k %= len(l)
        l = l[-k:] + l[:-k]
        l = np.array(l).reshape(len(grid), len(grid[0])).tolist()
        return l