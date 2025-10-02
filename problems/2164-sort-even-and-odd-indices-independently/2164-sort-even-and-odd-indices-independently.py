class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        l, m, n = [], [], len(nums)
        for i in range(n):
            if i & 1:
                l.append(nums[i])
            else:
                m.append(nums[i])
        l.sort(reverse = True)
        m.sort()
        for i in range(n):
            if i & 1:
                nums[i] = l[(i - 1) // 2]
            else:
                nums[i] = m[i // 2]
        return nums