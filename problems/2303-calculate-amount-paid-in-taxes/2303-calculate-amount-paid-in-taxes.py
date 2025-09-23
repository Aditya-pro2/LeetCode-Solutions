class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        s, p = 0.0, 0
        for i, j in brackets:
            if income >= i:
                s += ((i - p) * j) / 100
                p = i
            else:
                s += ((income - p) * j) / 100
                return s
        return s