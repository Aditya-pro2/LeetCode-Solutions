class Solution:
    def maxSum(self, nums: List[int]) -> int:
        d = defaultdict(int)
        s = -1
        for i in nums:
            x = max(str(i))
            if x in d:
                s = max(s, d[x] + i)
            d[x] = max(d[x], i)
        return s