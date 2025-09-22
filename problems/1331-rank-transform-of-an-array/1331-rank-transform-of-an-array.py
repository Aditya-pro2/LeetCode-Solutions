class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        l = sorted(set(arr))
        d = {j: i + 1 for i, j in enumerate(l)}
        return [d[i] for i in arr]