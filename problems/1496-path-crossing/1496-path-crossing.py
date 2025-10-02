class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        l = set()
        l.add((x, y))
        for i in path:
            if i == 'N':
                y += 1
            elif i == 'S':
                y -= 1
            elif i == 'E':
                x += 1
            else:
                x -= 1
            n = len(l)
            l.add((x, y))
            if n == len(l):
                return True
        return False