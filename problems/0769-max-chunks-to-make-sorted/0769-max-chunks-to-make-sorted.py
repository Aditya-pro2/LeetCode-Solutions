class Solution:
    def maxChunksToSorted(self, a: List[int]) -> int:
        c = m = 0
        for i in range(len(a)):
            m = max(m, a[i])
            c += (m == i)
        return c