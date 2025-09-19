class Solution:
    def repeatedCharacter(self, s: str) -> str:
        l = set()
        for i in s:
            x = l.copy()
            x.add(i)
            if len(x) == len(l):
                return i
            l = x.copy()
        return ""