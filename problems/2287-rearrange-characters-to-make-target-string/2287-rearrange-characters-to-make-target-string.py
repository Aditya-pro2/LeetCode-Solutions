class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        f, g, m = Counter(s), Counter(target), float('inf')
        for i in g:
            m = min(m, f[i] // g[i])
        return m