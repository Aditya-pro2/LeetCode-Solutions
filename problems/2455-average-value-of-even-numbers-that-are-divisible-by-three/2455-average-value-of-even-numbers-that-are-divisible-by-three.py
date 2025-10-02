class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s = c = 0
        for i in nums:
            if i % 6 == 0:
                s += i
                c += 1
        return 0 if c == 0 else s // c