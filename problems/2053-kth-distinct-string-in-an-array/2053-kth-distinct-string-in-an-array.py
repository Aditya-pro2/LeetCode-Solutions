class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = 0
        for i in arr:
            if arr.count(i) == 1:
                c += 1
            if c == k:
                return i
        return ""