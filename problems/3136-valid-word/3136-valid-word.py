class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 3:
            return False
        d = v = c = 0
        for i in s:
            if i.isdigit():
                d += 1
            elif i.isalpha():
                if i in "aeiouAEIOU":
                    v += 1
                else:
                    c += 1
        return ((d + v + c == len(s)) and v >= 1 and c >= 1)