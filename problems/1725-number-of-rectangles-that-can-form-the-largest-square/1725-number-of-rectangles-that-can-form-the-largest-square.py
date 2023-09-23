class Solution:
    def countGoodRectangles(self, r: List[List[int]]) -> int:
        x = []
        for i in r:
            x.append(min(i))
        l = max(x)
        return x.count(l)