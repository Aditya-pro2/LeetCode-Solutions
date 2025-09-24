class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n, x = len(nums), 0
        l = [0] * (n + 1)
        for i in nums:
            l[min(n, i)] += 1
        for i in range(n, 0, -1):
            x += l[i]
            if i == x:
                return i
        return -1