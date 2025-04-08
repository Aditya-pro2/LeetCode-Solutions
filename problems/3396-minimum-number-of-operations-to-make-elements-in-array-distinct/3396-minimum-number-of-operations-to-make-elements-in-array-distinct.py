class Solution:
    def minimumOperations(self, a: List[int]) -> int:
        c = 0
        while len(set(a)) != len(a):
            if len(a) > 3:
                a = a[3:]
            else:
                a = []
            c += 1
        return c