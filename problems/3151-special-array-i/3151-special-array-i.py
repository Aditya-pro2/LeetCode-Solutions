class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l = ['e' if i % 2 == 0 else 'o' for i in nums]
        for i in range(1, len(l)):
            if l[i] == l[i - 1]:
                return False
        return True