class Solution:
    def checkString(self, s: str) -> bool:
        n, x = len(s), s.count("a")
        return s == ("a" * x + "b" * (n - x))