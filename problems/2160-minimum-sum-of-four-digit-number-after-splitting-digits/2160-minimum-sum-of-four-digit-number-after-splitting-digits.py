class Solution:
    def minimumSum(self, n: int) -> int:
        s = sorted(list(str(n)))
        s[1], s[2] = s[2], s[1]
        return int("".join(s[:2])) + int("".join(s[2:]))