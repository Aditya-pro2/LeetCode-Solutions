class Solution:
    def maxWidthOfVerticalArea(self, a: List[List[int]]) -> int:
        x = [x0 for x0, _ in sorted(a)]
        return max([x[i + 1] - x[i] for i in range(len(x) - 1)])