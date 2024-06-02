class Solution:
    def matrixReshape(self, a: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(a), len(a[0])
        if m * n != r * c:
            return a
        p = []
        for i in range(m):
            for j in range(n):
                p.append(a[i][j])
        x = []
        z = 0
        for i in range(r):
            l = []
            for j in range(c):
                l.append(p[z])
                z += 1
            x.append(l)
        return x