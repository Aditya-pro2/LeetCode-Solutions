class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for j in range(len(matrix[0])):
            x, y = [], False
            for i in range(len(matrix)):
                if matrix[i][j] == -1:
                    x.append(i)
                    y = True
            if y:
                m = max([matrix[i][j] for i in range(len(matrix))])
                for i in x:
                    matrix[i][j] = m
        return matrix