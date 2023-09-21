class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        x = s.split(" ")[:k]
        s = ""
        for i in x:
            s += i + " "
        return s[:-1]