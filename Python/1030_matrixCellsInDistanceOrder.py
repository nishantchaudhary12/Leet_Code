'''We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.

Additionally, we are given a cell in that matrix with coordinates (r0, c0).

Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from smallest distance to largest distance.
Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.
(You may return the answer in any order that satisfies this condition.)'''

import collections


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        visited = set()
        queue = collections.deque()
        queue.append((r0, c0))
        result = list()
        while queue:
            r, c = queue.popleft()
            if (r, c) not in visited:
                visited.add((r, c))
                result.append([r, c])
                if r + 1 < R and (r + 1, c) not in visited:
                    queue.append((r + 1, c))
                if c + 1 < C and (r, c + 1) not in visited:
                    queue.append((r, c + 1))
                if r - 1 >= 0 and (r - 1, c) not in visited:
                    queue.append((r - 1, c))
                if c - 1 >= 0 and (r, c - 1) not in visited:
                    queue.append((r, c - 1))
        return result
