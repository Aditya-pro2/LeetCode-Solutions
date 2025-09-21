class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        r1, c1, r2, c2 = ord(coordinate1[0]) - 97, int(coordinate1[1]), ord(coordinate2[0]) - 97, int(coordinate2[1])
        return ((r1 + c1) & 1) == ((r2 + c2) & 1)