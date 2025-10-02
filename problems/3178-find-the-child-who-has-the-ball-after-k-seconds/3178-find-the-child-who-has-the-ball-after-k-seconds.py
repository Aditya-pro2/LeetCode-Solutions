class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        n -= 1
        x, y = divmod(k, n)
        return n - y if x & 1 else y