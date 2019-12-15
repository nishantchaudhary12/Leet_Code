'''Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.'''

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.antiD = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.row[row] += 1 if player == 1 else -1
        self.col[col] += 1 if player == 1 else -1

        if row == col:
            self.diag += 1 if player == 1 else -1

        if row + col == self.n - 1:
            self.antiD += 1 if player == 1 else -1

        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diag) == self.n or abs(
                self.antiD) == self.n:
            return 1 if player == 1 else 2

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)