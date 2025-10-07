class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        f = Counter(str(n))
        x = min(f.values())
        m = float('inf')
        for i, j in f.items():
            if j == x:
                m = min(m, int(i))
        return m