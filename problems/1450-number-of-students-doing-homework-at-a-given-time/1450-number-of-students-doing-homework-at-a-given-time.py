class Solution:
    def busyStudent(self, a: List[int], b: List[int], x: int) -> int:
        n, c = len(a), 0
        for i in range(n):
            if a[i] <= x <= b[i]:
                c += 1
        return c