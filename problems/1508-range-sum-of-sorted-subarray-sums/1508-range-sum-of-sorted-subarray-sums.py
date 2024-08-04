class Solution:
    def rangeSum(self, nums: List[int], n: int, l: int, r: int) -> int:
        a = []
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                a.append(s)
        a.sort()
        return sum(a[l - 1 : r]) % 1000000007