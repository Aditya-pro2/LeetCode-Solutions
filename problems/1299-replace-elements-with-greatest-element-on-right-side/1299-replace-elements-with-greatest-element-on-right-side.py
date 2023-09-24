class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rev, maximum = arr[::-1], -1
        for i in range(len(rev)):
            rev[i], maximum = maximum, max(maximum, rev[i])
        return rev[::-1]