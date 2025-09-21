class Solution:
    def findKOr(self, nums: list[int], k: int) -> int:
        ans = 0
        for b in range(32):
            cnt = 0
            for x in nums:
                if x >> b & 1:
                    cnt += 1
            if cnt >= k:
                ans |= 1 << b
        return ans