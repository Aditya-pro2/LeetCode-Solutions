class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        n, f, m, c = len(s), [0,] * 26, 1000000007, 0
        for i in range(n):
            f[ord(s[i]) - 97] += 1
        while t >= 26:
            l = [0,] * 26
            for j in range(25):
                l[j + 1] = (f[j] + l[j + 1]) % m
                l[j] = (f[j] + l[j]) % m
            l[-1] = (f[-1] + l[-1]) % m
            l[0] = (f[-1] + l[0]) % m
            l[1] = (f[-1] + l[1]) % m
            f, t = l, t - 26
        for i in range(26):
            if t >= (26 - i):
                f[i] = (2 * f[i]) % m
            c = (c + f[i]) % m
        return c