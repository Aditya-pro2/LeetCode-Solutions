class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = list(str(n))
        s, x = 1, 0
        for i in a:
            s *= int(i)
            x += int(i)
        return s - x