class Solution:
    def hasGroupsSizeX(self, d: List[int]) -> bool:
        f = Counter(d)
        return gcd(*list(f.values())) != 1