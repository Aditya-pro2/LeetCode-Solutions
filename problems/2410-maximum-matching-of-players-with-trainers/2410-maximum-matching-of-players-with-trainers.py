class Solution:
    def matchPlayersAndTrainers(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        c = i = j = 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                c += 1
                i += 1
                j += 1
            else:
                j += 1
        return c