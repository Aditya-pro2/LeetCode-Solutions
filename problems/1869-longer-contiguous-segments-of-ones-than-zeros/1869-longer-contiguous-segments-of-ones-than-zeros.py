class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        t1 = t2 = m1 = m2 = 0
        for i in s:
            if i == '0':
                t1 += 1
                t2 = 0
            else:
                t1 = 0
                t2 += 1
            m1 = max(m1, t1)
            m2 = max(m2, t2)
        return m2 > m1