class Solution:
    def findPeaks(self, a: List[int]) -> List[int]:
        l = []
        for i in range(1, len(a) - 1):
            if a[i] > a[i - 1] and a[i] > a[i + 1]:
                l.append(i)
        return l