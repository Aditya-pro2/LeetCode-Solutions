class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        x, i, q, r = 0, 1, n // 8, n % 8
        while q > 0:
            x += 8 * i
            q -= 1
            i += 1
        x += r * i
        return x