class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        m = 1000000007
        l, x, c = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97], [1,] * (n + 1), 0
        for i in range(len(l)):
            if l[i] <= n:
                c += 1
        for i in range(2, n + 1):
            x[i] = i * x[i - 1]
        return (x[c] * x[n - c]) % m