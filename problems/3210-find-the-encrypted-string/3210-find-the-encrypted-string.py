class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        l = []
        n = len(s)
        for i in range(n):
            l.append(s[(i + k) % n])
        return "".join(l)