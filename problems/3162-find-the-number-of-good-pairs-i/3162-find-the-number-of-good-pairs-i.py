class Solution:
    def numberOfPairs(self, a: List[int], b: List[int], k: int) -> int:
        c = 0
        for i in a:
            for j in b:
                c += (i % (j * k) == 0)
        return c