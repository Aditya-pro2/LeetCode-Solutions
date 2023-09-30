class Solution:
    def finalString(self, s: str) -> str:
        l = []
        for x in s:
            if x == "i":
                l = l[::-1]
            else:
                l.append(x)
        return "".join(l)