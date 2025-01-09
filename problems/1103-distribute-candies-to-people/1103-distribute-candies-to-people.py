class Solution:
    def distributeCandies(self, s: int, n: int) -> List[int]:
        k, i = 1, 0
        l = [0,] * n
        while s > k:
            l[i] += k
            s -= k
            k += 1
            i = (i + 1) % n
        l[i] += s
        return l