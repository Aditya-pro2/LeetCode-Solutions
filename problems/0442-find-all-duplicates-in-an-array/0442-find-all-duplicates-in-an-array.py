class Solution:
    def findDuplicates(self, a: List[int]) -> List[int]:
        a.sort()
        l = []
        for i in range(len(a) - 1):
            if a[i] == a[i + 1]:
                l.append(a[i])
        return l