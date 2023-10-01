class Solution:
    def convertToTitle(self, n: int) -> str:
        l = []
        while n > 0:
            n -= 1
            l.append(chr((n % 26) + 65))
            n = n // 26
        return "".join(l)[::-1]