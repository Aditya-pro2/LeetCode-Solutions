class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        mr, mc = m, n
        for i in ops:
            mr, mc = min(mr, i[0]), min(mc, i[1])
        return mr * mc