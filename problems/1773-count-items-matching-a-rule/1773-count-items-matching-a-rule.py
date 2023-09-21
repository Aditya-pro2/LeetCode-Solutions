class Solution:
    def countMatches(self, items: List[List[str]], k: str, v: str) -> int:
        x = ["type", "color", "name"].index(k)
        c = 0
        for i in items:
            if i[x] == v:
                c += 1
        return c