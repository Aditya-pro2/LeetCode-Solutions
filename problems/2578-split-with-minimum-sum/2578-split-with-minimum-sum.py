class Solution:
    def splitNum(self, n: int) -> int:
        a = sorted([int(i) for i in str(n)])
        b, c = '', ''
        for i, x in enumerate(a):
            if i % 2 == 0:
                b += str(x)
            else:
                c += str(x)
        return int(b) + int(c)