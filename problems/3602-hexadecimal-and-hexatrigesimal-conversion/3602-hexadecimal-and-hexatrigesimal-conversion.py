class Solution:
    def concatHex36(self, n: int) -> str:
        def hext(n, b):
            if n == 0:
                return "0"
            ch, ans = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", ""
            while n > 0:
                r = n % b
                ans = ch[r] + ans
                n //= b
            return ans
        return hext(n * n, 16) + hext(n ** 3, 36)