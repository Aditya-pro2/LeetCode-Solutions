class Solution:
    def countDigits(self, num: int) -> int:
        x, c = str(num), 0
        for i in x:
            if num % int(i) == 0:
                c += 1
        return c