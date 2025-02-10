class Solution:
    def clearDigits(self, s: str) -> str:
        l = []
        for i in s:
            if i.isdigit():
                if l:
                    l.pop()
            else:
                l.append(i)
        return "".join(l)