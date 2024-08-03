class Solution:
    def canBeEqual(self, t: List[int], a: List[int]) -> bool:
        return Counter(t) == Counter(a)