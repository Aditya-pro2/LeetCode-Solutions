class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            t = str(i)
            for j in t:
                l.append(int(j))
        return l