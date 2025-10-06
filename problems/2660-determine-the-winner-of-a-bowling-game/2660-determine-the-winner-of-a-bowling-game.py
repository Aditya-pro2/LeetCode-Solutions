class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        player1 = [0, 0] + player1
        player2 = [0, 0] + player2
        n = len(player1)
        a = b = 0
        for i in range(2, n):
            a += (2 * player1[i] if player1[i - 1] == 10 or player1[i - 2] == 10 else player1[i])
            b += (2 * player2[i] if player2[i - 1] == 10 or player2[i - 2] == 10 else player2[i])
        return 1 if a > b else 2 if a < b else 0