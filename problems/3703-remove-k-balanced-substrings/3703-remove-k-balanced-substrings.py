class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        x = '(' * k + ')' * k
        n = len(x)
        while x in s:
            i = s.find(x)
            s = s[:i] + s[(i + n):]
        return s