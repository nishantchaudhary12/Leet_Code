'''You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path,
they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.
The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.'''

from collections import defaultdict


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        connected = defaultdict(list)
        for each in paths:
            connected[each[0]].append(each[1])
            connected[each[1]].append(each[0])

        # print(connected)
        result = [0] * N
        for i in range(1, N + 1):
            choices = {1, 2, 3, 4}
            if i in connected:
                for j in connected[i]:
                    choices.discard(result[j - 1])
            result[i - 1] = choices.pop()
        # print(result)
        return result
