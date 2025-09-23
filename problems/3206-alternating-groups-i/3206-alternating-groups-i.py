class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        c, n = 0, len(colors)
        for i in range(n):
            if colors[i] != colors[i - 1] and colors[i] != colors[(i + 1) % n]:
                c += 1
        return c