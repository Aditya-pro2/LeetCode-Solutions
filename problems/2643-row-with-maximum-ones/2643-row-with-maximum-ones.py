class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        a = []
        for i in mat:
            a.append(i.count(1))
        c = max(a)
        x = a.index(c)
        return [x, c]