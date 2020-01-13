'''Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once.'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(arr, word, i, j):
            if arr[i][j] == word: return True
            if arr[i][j] == word[0]:
                arr[i][j] = ''
                for each in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= each[0] < m and 0 <= each[1] < n and arr[each[0]][each[1]] == word[1]:
                        if search(arr, word[1:], each[0], each[1]):
                            return True
            arr[i][j] = word[0]
            return False

        m = len(board)
        n = len(board[0])
        if not word:
            return True
        if not board:
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and search(board, word, i, j):
                    return True
        return False