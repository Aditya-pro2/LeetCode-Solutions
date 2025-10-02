class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        shift = k % len(mat[0])
        for i, row in enumerate(mat):
            if i % 2 == 0:
                row_s = row[shift:] + row[:shift]
            else:
                row_s = row[-shift:] + row[:-shift]
            if row_s != row:
                return False
        return True