class Solution:
    def getSmallestString(self, s: str) -> str:
        s = list(map(int, s))
        for i in range(len(s) - 1):
            if s[i] > s[i + 1] and (s[i] - s[i + 1]) % 2 == 0:
                s[i], s[i + 1] = s[i + 1], s[i]
                break
        return "".join(list(map(str, s)))