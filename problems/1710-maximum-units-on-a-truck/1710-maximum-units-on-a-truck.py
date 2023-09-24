class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], a: int) -> int:
        x = sorted(boxTypes, key = lambda x: x[1], reverse = True)
        s = 0
        for i in x:
            if a < i[0]:
                s += (a * i[1])
                break
            s += (i[0] * i[1])
            a -= i[0]
        return s