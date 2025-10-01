class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        l = []
        for i in range(len(grid)):
            if i & 1:
                l += grid[i][::-1]
            else:
                l += grid[i]
        return [l[i] for i in range(0, len(l), 2)]