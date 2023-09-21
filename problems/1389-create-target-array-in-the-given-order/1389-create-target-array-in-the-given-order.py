class Solution:
    def createTargetArray(self, nums: List[int], x: List[int]) -> List[int]:
        n = len(nums)
        a = []
        for i in range(n):
            if x[i] == len(a):
                a.append(nums[i])
            else:
                a = a[:x[i]] + [nums[i]] + a[x[i]:]
            print(a)
        return a