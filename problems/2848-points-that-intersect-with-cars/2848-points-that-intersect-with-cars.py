class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        x = []
        for i, j in nums:
            x.extend(range(i, j + 1))
        a = set(x)
        return len(a)