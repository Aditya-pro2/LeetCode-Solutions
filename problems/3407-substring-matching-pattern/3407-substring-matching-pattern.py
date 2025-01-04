class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        x, y = p.split('*')
        c = -1
        for i in range(len(s) - len(x) + 1):
            if s[i : i + len(x)] == x:
                c = i + len(x)
                break
        if c == -1:
            return False
        for i in range(c, len(s) - len(y) + 1):
            if s[i : i + len(y)] == y:
                return True
        return False