class Solution:
    def addToArrayForm(self, a: List[int], k: int) -> List[int]:
        c = 0
        a = [0,] * (len(str(k)) - len(a)) + a
        for x in range(-1, -len(a) - 1, -1):
            s = a[x] + (k % 10) + c
            a[x] = s % 10
            c = s // 10
            x -= 1
            k //= 10
        if c > 0:
            a = [c] + a
        return a