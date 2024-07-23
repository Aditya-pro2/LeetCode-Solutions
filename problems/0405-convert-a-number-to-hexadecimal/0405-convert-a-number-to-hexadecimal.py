class Solution:
    def toHex(self, n: int) -> str:
        if n == 0:
            return "0"
        s, a = "0123456789abcdef",""
        while n != 0 and len(a) < 8:
            a = s[n & 15] + a
            n >>= 4
        return a