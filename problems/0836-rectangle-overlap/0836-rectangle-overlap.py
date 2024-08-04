class Solution:
    def isRectangleOverlap(self, x: List[int], y: List[int]) -> bool:
        return x[2] > y[0] and x[3] > y[1] and x[0] < y[2] and x[1] < y[3]