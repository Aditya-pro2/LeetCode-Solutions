class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        x = y = z = 0
        while n:
            if n & 1:
                if x & 1:
                    z += 1
                else:
                    y += 1
            n >>= 1
            x += 1
        return [y, z]