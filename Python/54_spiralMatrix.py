'''Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = list()
        x = len(matrix)
        if x > 0:
            y = len(matrix[0])
            i, j = 0, 0         #starting index
            while i < x and j < y:
                for z in range(j, y):
                    result.append(matrix[i][z])
                i += 1

                for z in range(i, x):
                    result.append(matrix[z][y-1])
                y -= 1

                if i < x:
                    for z in range(y-1, j-1, -1):
                        result.append(matrix[x-1][z])
                x -= 1

                if j < y:
                    for z in range(x-1, i-1, -1):
                        result.append(matrix[z][j])
                j += 1

        return result