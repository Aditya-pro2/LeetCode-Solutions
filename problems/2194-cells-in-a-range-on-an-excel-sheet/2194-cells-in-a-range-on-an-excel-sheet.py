class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        a, b, c, d = ord(s[0]), int(s[1]), ord(s[3]), int(s[4])
        l = []
        for i in range(a, c + 1):
            for j in range(b, d + 1):
                l.append(chr(i) + str(j))
        return l