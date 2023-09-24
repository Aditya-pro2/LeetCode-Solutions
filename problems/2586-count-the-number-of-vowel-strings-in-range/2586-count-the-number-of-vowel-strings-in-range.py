class Solution:
    def vowelStrings(self, x: List[str], left: int, right: int) -> int:
        c = 0
        for i in range(left, right + 1):
            if x[i][0] in "aeiou" and x[i][-1] in "aeiou":
                c += 1
        return c