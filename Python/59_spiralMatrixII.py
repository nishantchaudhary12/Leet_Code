'''Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for i in range(n)]
        arr = [i for i in range(1,n*n+1)]
        i,j,k = 0,0,0
        x, y = n, n
        while i < x and j < y:

            for l in range(j,y):
                result[i][l] = arr[k]
                k += 1
            i += 1

            for l in range(i,x):
                result[l][y-1] = arr[k]
                k += 1
            y -= 1

            if i < x:
                for l in range(y-1, j-1, -1):
                    result[x-1][l] = arr[k]
                    k += 1
                x -= 1

            if j < y:
                for l in range(x-1, i-1, -1):
                    result[l][j] = arr[k]
                    k += 1
                j += 1

        return result