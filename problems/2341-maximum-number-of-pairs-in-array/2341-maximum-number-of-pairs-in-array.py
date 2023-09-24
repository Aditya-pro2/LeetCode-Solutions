class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        x = set(nums)
        a = b = 0
        for i in x:
            c = nums.count(i)
            a += (c // 2)
            b += (c % 2)
        return [a, b]