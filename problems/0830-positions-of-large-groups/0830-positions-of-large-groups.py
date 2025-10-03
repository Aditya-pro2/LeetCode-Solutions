class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        l = []
        x = ""
        for i in range(len(s)):
            if x == "" or x[-1] == s[i]:
                x += s[i]
            else:
                if len(x) >= 3:
                    l.append([i - len(x), i - 1])
                x = s[i]
        i += 1
        if len(x) >= 3:
            l.append([i - len(x), i - 1])
        return l