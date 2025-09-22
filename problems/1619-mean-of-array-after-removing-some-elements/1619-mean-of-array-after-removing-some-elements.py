class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        l = len(arr)
        n = l // 20
        return sum(arr[n: -n]) / (l - 2 * n)