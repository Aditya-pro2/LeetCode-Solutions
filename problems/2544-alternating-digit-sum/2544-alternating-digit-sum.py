class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s, c, p = str(n), 0, 1
        for i in s:
            c += (int(i) * p)
            p *= (-1)
        return c