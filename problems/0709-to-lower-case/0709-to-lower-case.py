class Solution:
    def toLowerCase(self, s: str) -> str:
        x = s[:]
        for i in range(len(x)):
            if x[i].isupper():
                s = s.replace(x[i], chr(ord(x[i]) + 32))
        return s