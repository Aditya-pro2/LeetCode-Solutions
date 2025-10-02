class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n, mod = divmod(n, 2)
        while n:
            if n % 2 == mod:
                return False
            n, mod = divmod(n, 2)
        return True