class Solution:
    def countPoints(self, rings: str) -> int:
        r, g, b, x = [False,] * 10, [False,] * 10, [False,] * 10, 0
        for i in range(1, len(rings), 2):
            match (rings[i - 1]):
                case 'R':
                    r[int(rings[i])] = True
                case 'G':
                    g[int(rings[i])] = True
                case 'B':
                    b[int(rings[i])] = True
        for i in range(10):
            if r[i] and g[i] and b[i]:
                x += 1
        return x