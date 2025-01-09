class Solution:
    def prefixCount(self, l: List[str], s: str) -> int:
        return sum(i.startswith(s) for i in l)