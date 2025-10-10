class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        m = defaultdict(list)
        for x, y in points:
            m[x].append(y)
        for key in m.keys():
            m[key].sort()
        ans = []
        for cx, cy, r in queries:
            inside = 0
            for dx in range(-r, r + 1):
                dy = math.sqrt((r ** 2) - (dx ** 2))
                x = cx + dx
                lower_y = cy - dy
                upper_y = cy + dy
                lower_ind = bisect.bisect_left(m[x], lower_y)
                upper_ind = bisect.bisect_right(m[x], upper_y)
                inside += upper_ind - lower_ind
            ans.append(inside)
        return ans