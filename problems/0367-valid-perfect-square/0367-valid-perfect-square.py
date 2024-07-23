from math import sqrt
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = sqrt(num)
        return x == int(x)