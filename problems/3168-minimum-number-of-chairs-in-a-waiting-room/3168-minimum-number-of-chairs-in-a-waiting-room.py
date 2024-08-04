class Solution:
    def minimumChairs(self, s: str) -> int:
        a = c = 0
        for i in s:
            c += 1 if i == 'E' else -1
            a = max(a, c)
        return a