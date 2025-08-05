class Solution:
    def isBalanced(self, num: str) -> bool:
        if len(num) & 1:
            num += "0"
        x = y = 0
        for i in range(0, len(num), 2):
            x += int(num[i])
            y += int(num[i + 1])
        return x == y