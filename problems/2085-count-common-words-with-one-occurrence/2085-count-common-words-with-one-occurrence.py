class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        m1, m2, c, j = {}, {}, 0, 0
        for i in words1:
            m1[i] = m1.get(i, 0) + 1        
        for j in words2:
            m2[j] = m2.get(j, 0) + 1
        for k, v in m1.items():
            j = m2.get(k, 0)
            if v == j == 1:
                c += 1
        return c