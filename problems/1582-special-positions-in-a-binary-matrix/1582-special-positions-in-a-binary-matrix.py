class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n, ans = len(mat), len(mat[0]), 0
        col = [False] * n
        for i in range(m):
            idx = [j for j in range(n) if mat[i][j] == 1]
            if len(idx) == 1 and not col[idx[0]]:
                col[idx[0]] = True
                if all(mat[k][idx[0]] == 0 for k in range(i + 1, m)):
                    ans += 1
            else:
                for j in idx:
                    col[j] = True
        return ans