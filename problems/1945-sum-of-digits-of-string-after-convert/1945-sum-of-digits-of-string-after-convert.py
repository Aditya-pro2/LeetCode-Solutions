class Solution:
    def getLucky(self, s: str, k: int) -> int:
        x, c = "", 0
        for i in s:
            x += str(ord(i) - 96)
        for _ in range(k):
            for i in x:
                c += int(i)
            x = str(c)
            c = 0
        return int(x)