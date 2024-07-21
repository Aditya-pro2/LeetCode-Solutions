class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n == k:
            return 0
        n, k = bin(n), bin(k)
        a, b = len(n), len(k)
        if a < b:
            n = "0b" + "0" * (b - a) + n[2:]
        else:
            k = "0b" + "0" * (a - b) + k[2:]
        c = 0
        for i in range(2, len(n)):
            if n[i] == "0" and k[i] == "1":
                return -1
            if n[i] == "1" and k[i] == "0":
                c += 1
        return c if c > 0 else -1