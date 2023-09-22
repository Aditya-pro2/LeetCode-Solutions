class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        x = len(words)
        if x != len(s):
            return False
        for i in range(x):
            if words[i][0] != s[i]:
                return False
        return True