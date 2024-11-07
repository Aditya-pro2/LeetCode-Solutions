class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = sum(1 for j in candidates if j & (1 << i))
            ans = max(ans, cnt)
        return ans