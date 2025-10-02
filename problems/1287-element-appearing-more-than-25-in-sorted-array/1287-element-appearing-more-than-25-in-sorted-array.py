class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        f, n = Counter(arr), len(arr)
        for i in f:
            if f[i] > n / 4:
                return i
        return -1