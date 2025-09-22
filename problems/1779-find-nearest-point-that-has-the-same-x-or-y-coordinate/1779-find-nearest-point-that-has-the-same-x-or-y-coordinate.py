class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        c, d = -1, float('inf')
        for i in range(len(points)):
            if x == points[i][0] and d > abs(y - points[i][1]):
                c, d = i, abs(y - points[i][1])
            if y == points[i][1] and d > abs(x - points[i][0]):
                c, d = i, abs(x - points[i][0])
        return c