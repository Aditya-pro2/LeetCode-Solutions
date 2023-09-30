class Solution:
    def countAsterisks(self, s: str) -> int:
        a = b = 0
        for i in s:
            if i == "|":
                b += 1
            if i == "*" and b % 2 == 0:
                a += 1
        return a