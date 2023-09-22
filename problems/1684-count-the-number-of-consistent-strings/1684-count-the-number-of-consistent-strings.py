class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        k = 0
        for i in words:
            c = 0
            for j in allowed:
                c += i.count(j)
            if c == len(i):
                k += 1
        return k