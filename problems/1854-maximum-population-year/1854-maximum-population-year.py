class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        l = []
        for i, j in logs:
            l.append((i, 1))
            l.append((j, -1))
        l.sort()
        p = m = y = 0
        for i, j in l:
            p += j
            if p > m:
                m = p
                y = i
        return y