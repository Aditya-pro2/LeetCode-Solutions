class Solution:
    def findDuplicate(self, a: List[int]) -> int:
        a.sort()
        i = 1
        for j in a:
            if j == a[i]:
                return j
            i += 1