class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        topArray = []
        tmp, Sum = 0, sum(nums)
        for i in nums:
            tmp += i
            topArray.append(i)
            if 2*tmp > Sum:
                return topArray