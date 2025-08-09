class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = list(s)
        for i in range(len(s)):
            l[i] = l[~i] = min(l[i], l[~i])
        return ''.join(l)