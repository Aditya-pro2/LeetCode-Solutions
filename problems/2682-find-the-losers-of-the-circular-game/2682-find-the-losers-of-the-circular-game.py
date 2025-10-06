class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        t, i = 1, 0
        seen = [False for _ in range(n)]
        while not seen[i]:
            seen[i] = True
            i = (i + (t * k)) % n
            t += 1
        return [i + 1 for i, s in enumerate(seen) if not s]