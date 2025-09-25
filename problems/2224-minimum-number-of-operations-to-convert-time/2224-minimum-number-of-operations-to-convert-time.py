class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        a, b = 60 * int(current[0:2]) + int(current[3:5]), 60 * int(correct[0:2]) + int(correct[3:5])
        x, c = b - a, 0
        for i in [60, 15, 5, 1]:
            c += x // i
            x %= i
        return c