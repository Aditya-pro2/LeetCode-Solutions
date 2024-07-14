class Solution:
    def splitWordsBySeparator(self, w: List[str], s: str) -> List[str]:
        a = []
        for i in w:
            x = i.split(s)
            for j in x:
                if len(j) > 0:
                    a.append(j)
        return a