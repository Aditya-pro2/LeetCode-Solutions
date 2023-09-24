class Solution:
    def twoOutOfThree(self, a: List[int], b: List[int], c: List[int]) -> List[int]:
        x, l = set(a + b + c), []
        for i in x:
            if (i in a and i in b) or (i in b and i in c) or (i in a and i in c):
                l.append(i)
        return l