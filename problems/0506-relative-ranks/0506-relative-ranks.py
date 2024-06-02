class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a = sorted(score, reverse = True)
        x = ["a", ] * len(a)
        for i in range(len(a)):
            p = score.index(a[i])
            if i == 0:
                x[p] = "Gold Medal"
            elif i == 1:
                x[p] = "Silver Medal"
            elif i == 2:
                x[p] = "Bronze Medal"
            else:
                x[p] = str(i + 1)
        return x