class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        l, x = [], 1
        while n > 0:
            d = n % 10
            if d != 0:
                l = [d * x] + l
            x *= 10
            n //= 10
        return l