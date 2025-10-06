class Solution:
    def reorderSpaces(self, text: str) -> str:
        w = text.split()
        cnt = len(w)
        s = text.count(' ')
        g = 0 if cnt == 1 else s // (cnt - 1)
        x = s - g * (cnt - 1)
        return (' ' * g).join(w) + ' ' * x