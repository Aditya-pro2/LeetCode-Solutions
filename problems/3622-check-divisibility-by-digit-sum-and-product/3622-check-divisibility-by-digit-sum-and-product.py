class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s, p = 0, 1
        l = list(map(int, str(n)))
        for i in l:
            s += i
            p *= i
        return n % (s + p) == 0