class Solution:
    def restoreString(self, s: str, p: List[int]) -> str:
        x = ""
        for i in range(len(p)):
            x = x + s[p.index(i)]
        return x