class Solution:
    def threeConsecutiveOdds(self, a: List[int]) -> bool:
        def fun(x):
            return x % 2 == 1
        for i in range(len(a) - 2):
            if fun(a[i]) and fun(a[i + 1]) and fun(a[i + 2]):
                return True
        return False