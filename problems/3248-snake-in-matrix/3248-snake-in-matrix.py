class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i, j = 0, 0
        moves = {'UP': [0, -1], 'DOWN': [0, 1], 'LEFT': [-1, 0], 'RIGHT': [1, 0]}
        for command in commands:
            move = moves.get(command)
            i += move[1]
            j += move[0]
        return (i * n) + j