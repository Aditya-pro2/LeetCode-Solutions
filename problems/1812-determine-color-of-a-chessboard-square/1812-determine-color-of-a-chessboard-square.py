class Solution:
    def squareIsWhite(self, c: str) -> bool:
        if c[0] in "aceg":
            if int(c[1]) % 2 == 1:
                return False
            return True
        else:
            if int(c[1]) % 2 == 0:
                return False
            return True