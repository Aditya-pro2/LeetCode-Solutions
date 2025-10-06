class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans, x = 0, "01"
        while len(x) <= len(s):
            if x in s: 
                ans = len(x)
            x = '0' + x + '1'
        return ans