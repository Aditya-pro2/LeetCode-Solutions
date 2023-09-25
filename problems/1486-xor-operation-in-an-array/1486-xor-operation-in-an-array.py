class Solution:
    def xorOperation(self, n: int, x: int) -> int:
        a, p = [x], x
        for i in range(1, n):
            a.append(x + 2 * i)
            p ^= a[i]
        return p