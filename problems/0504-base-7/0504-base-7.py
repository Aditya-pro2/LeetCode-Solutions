class Solution:
    def convertToBase7(self, n: int) -> str:
        if n == 0:
            return "0"
        s = ""
        k = -1 if n < 0 else 1
        n = abs(n)
        while n > 0:
            s = str(n % 7) + s
            n = n // 7
        return "-" * (k == -1) + s