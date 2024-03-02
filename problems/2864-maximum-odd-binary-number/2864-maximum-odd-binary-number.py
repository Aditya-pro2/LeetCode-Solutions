class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        x, n = s.count('1'), len(s)
        l, m = ['1', ], ['0', ]
        return "".join(l * (x - 1) + m * (n - x) + l)