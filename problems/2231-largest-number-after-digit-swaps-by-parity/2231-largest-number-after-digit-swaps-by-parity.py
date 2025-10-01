class Solution:
    def largestInteger(self, num: int) -> int:
        s = list(str(num))
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[j] > s[i] and (int(s[j]) - int(s[i])) % 2 == 0:
                    s[i], s[j] = s[j], s[i]
        return int("".join(s))