class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            x = i
            while x > 0:
                s += (x % 10)
                x //= 10
        return abs(s - sum(nums))