class Solution:
    def binaryGap(self, n: int) -> int:
        n, l, x = bin(n)[2:], [], 0
        l = [i for i in range(len(n)) if n[i] == "1"]
        for i in range(1, len(l)):
            x = max(x, l[i] - l[i - 1])
        return x