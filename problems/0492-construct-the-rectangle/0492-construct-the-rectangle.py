class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        x = int(sqrt(area))
        l = []
        for i in range(1, x + 1):
            if area % i == 0:
                l = [area // i, i]
        return l