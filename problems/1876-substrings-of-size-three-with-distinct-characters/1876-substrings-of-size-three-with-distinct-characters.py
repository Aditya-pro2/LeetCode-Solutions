class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c = 0
        for i in range(len(s) - 2):
            x = s[i : (i + 3)]
            c += (len(x) == len(set(x)))
        return c