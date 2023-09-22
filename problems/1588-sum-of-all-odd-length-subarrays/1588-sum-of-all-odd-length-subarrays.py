class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s, l = 0, len(arr)
        for i in range(l):
            for j in range(i, l, 2):
                for k in range(i, j + 1, 1):
                    s += arr[k]
        return s