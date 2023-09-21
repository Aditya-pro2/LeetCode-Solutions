class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        m = []
        for i in s:
            c = i.count(' ') + 1
            m.append(c)
        return max(m)