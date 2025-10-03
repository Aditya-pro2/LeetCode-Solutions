class Solution:
    def isFascinating(self, n: int) -> bool:
        n = sorted(str(n) + str(2 * n) + str(3 * n))
        return "".join(n) == "123456789"