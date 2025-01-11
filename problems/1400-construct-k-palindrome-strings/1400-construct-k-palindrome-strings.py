class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return (freq:=Counter(s)) and sum(f&1 for f in freq.values())<=k<=len(s)