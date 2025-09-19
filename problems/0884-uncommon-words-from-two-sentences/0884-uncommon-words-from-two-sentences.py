class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        w = Counter(s1.split() + s2.split())
        return [i for i in w if w[i] == 1]