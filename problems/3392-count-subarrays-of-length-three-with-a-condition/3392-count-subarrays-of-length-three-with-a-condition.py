class Solution:
    def countSubarrays(self, a: List[int]) -> int:
        c = 0
        for i in range(len(a) - 2):
            if (a[i] + a[i + 2]) == (a[i + 1] / 2):
                c += 1
        return c