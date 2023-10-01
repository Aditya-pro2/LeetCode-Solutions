class Solution:
    def titleToNumber(self, c: str) -> int:
        a = b = 0
        for i in c[::-1]:
            a += (ord(i) - 64) * 26 ** b
            b += 1
        return a