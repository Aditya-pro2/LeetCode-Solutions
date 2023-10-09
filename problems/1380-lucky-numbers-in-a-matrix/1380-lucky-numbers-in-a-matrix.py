class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])
        lr=[min(i) for i in matrix]
        lc=[]
        ans=[]
        for i in range(n):
            c=[k[i] for k in matrix]
            lc.append(max(c))
        for i in lr:
            if i in lc:ans.append(i)
        return ans