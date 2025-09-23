class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        info = {}
        ans = -1
        for i in range(len(s)): 
            if s[i] in info: 
                ans = max(ans, i - info[s[i]] - 1)
            else: 
                info[s[i]] = i
        return ans