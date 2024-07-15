class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        m = max(len(i) for i in s)
        a = []
        for i in range(m):
            x = ''
            for j in s:
                if i < len(j):
                    x += j[i]
                else:
                    x += ' '
            a.append(x.rstrip())
        return a