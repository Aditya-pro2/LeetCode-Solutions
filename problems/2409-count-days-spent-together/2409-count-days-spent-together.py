class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def getDate(x):
            m, d = int(x[:2]), int(x[3:])
            return sum(l[: (m - 1)]) + d
        return max(0, getDate(min(leaveAlice, leaveBob)) - getDate(max(arriveAlice, arriveBob)) + 1)