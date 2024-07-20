class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        s = ["Alice", "Bob"]
        if not (x > 0 and y > 3):
            return s[1]
        c = 0
        while True:
            x, y = x - 1, y - 4
            if x > 0 and y > 3:
                c += 1
            else:
                return s[c % 2 == 1]