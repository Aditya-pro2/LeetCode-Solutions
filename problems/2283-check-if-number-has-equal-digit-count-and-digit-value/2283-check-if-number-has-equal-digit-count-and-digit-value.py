class Solution:
    def digitCount(self, num: str) -> bool:
        d = {}
        for i in num:
            i = int(i)
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        n = len(num)
        for i in range(n):
            if i in d:
                if d[i] != int(num[i]):
                    return False
            else:
                if int(num[i]) != 0:
                    return False
        return True