class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        x, n = sorted(heights), []
        for i in x[::-1]:
            n.append(names[heights.index(i)])
        return n