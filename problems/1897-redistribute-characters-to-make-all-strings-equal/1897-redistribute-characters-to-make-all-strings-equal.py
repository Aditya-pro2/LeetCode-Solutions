class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        l = len(words)
        s = "".join(words)
        x = set(s)
        for i in x:
            if s.count(i) % l != 0:
                return False
        return True