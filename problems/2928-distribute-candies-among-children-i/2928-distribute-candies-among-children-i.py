class Solution:
    def distributeCandies(self, n: int, l: int) -> int:
        c = lambda x: ((x * (x - 1)) // 2)
        if n > (3 * l):
            return 0
        a = c(n + 2)
        if n > l:
            a = a - (3 * c(n - l + 1))
        if n - 2 >= (2 * l):
            a = a + (3 * c(n - (2 * l)))
        return a