class Solution:
    def distributeCandies(self, a: List[int]) -> int:
        x, y = len(a) // 2, len(set(a))
        return min(x, y)