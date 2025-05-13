class Solution:
    def dayOfYear(self, date: str) -> int:
        l = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y, m, d, s = int(date[:4]), int(date[5:7]), int(date[8:]), 0
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            l[2] = 29
        for i in range(m):
            s += l[i]
        s += d
        return s