class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s = set()
        for i in ranges:
            for j in range(i[0], i[1] + 1):
                if j not in s and j in range(left, right + 1):
                    s.add(j)
            if len(s) - 1 == right - left:
                return True
        return False