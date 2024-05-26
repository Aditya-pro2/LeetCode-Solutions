class Solution:
    def compressedString(self, a: str) -> str:
        l = []
        x = 1
        for i in range(len(a) - 1):
            if a[i] == a[i + 1] and x < 9:
                x += 1
            else:
                l.append(str(x))
                l.append(a[i])
                x = 1
        if len(a) == 1 or (len(a) >= 2 and a[-1] != a[-2]) or x != 1 or (len(a) >= 2 and l[-2] == "9" and a[-1] == a[-2]):
            l.append(str(x))
            l.append(a[-1])
        return "".join(l)