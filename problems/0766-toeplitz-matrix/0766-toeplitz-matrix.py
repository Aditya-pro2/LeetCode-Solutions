class Solution:
    def isToeplitzMatrix(self, a: List[List[int]]) -> bool:
        for i in range(len(a) - 1):
            for j in range(len(a[i]) - 1):
                if a[i][j] != a[i + 1][j + 1]:
                    return False
        return True