class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) == sorted(s2):
            for i, j in zip(range(0, len(s1)), range(2, len(s2))):
                if s1[i] == s2[j] and s1[j] == s2[i]:
                    return True
        return False