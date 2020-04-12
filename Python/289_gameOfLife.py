'''According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised
by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its
eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births
and deaths occur simultaneously.'''


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        indx1 = list()
        indx0 = list()
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                currCount = 0
                if i-1 >= 0 and board[i-1][j] == 1:
                    currCount += 1
                if i-1 >= 0:
                    if j-1 >= 0 and board[i-1][j-1] == 1:
                        currCount += 1
                    if j+1 < n and board[i-1][j+1] == 1:
                        currCount += 1
                if i+1 < m and board[i+1][j] == 1:
                    currCount += 1
                if i+1 < m:
                    if j-1 >= 0 and board[i+1][j-1] == 1:
                        currCount += 1
                    if j+1 < n and board[i+1][j+1] == 1:
                        currCount += 1
                if j-1 >= 0 and board[i][j-1] == 1:
                    currCount += 1
                if j+1 < n and board[i][j+1] == 1:
                    currCount += 1
                # print(currCount)
                if board[i][j] == 1:
                    if currCount < 2:
                        indx1.append((i, j))
                    elif currCount > 3:
                        indx1.append((i,j))
                else:
                    if currCount == 3:
                        indx0.append((i,j))
        # print(indx1)
        # print(indx0)
        for i, j in indx0:
            board[i][j] = 1
        for i, j in indx1:
            board[i][j] = 0