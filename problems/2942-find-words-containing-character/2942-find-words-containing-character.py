class Solution:
    def findWordsContaining(self, a: List[str], x: str) -> List[int]:
        l = []
        for i in range(len(a)):
            if x in a[i]:
                l.append(i)
        return l