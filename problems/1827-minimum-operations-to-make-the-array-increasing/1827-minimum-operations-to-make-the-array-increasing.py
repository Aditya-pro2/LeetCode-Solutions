class Solution:
    def minOperations(self, x: List[int]) -> int:
        c = 0
        for i in range(1, len(x)):
            if x[i] <= x[i - 1]:
                c += (x[i - 1] + 1 - x[i])
                x[i] = x[i - 1] + 1      
        return c