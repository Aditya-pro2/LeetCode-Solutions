class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        s = set(word1 + word2)
        c = Counter(word1)
        c1 = Counter(word2)
        result = True
        for i in s:
            if abs(c[i] - c1[i]) <= 3:
                continue
            else:
                result = result & False
        return result