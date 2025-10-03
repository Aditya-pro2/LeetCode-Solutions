class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        x = ""
        for i in words:
            x += i
            if x == s:
                return True
        return False