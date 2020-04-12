'''Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.'''


class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        possible_times = [[A[0] * 10 + A[1], A[2] * 10 + A[3]],
                          [A[0] * 10 + A[1], A[3] * 10 + A[2]],
                          [A[0] * 10 + A[2], A[1] * 10 + A[3]],
                          [A[0] * 10 + A[2], A[3] * 10 + A[1]],
                          [A[0] * 10 + A[3], A[1] * 10 + A[2]],
                          [A[0] * 10 + A[3], A[2] * 10 + A[1]],

                          [A[1] * 10 + A[0], A[2] * 10 + A[3]],
                          [A[1] * 10 + A[0], A[3] * 10 + A[2]],
                          [A[1] * 10 + A[2], A[0] * 10 + A[3]],
                          [A[1] * 10 + A[2], A[3] * 10 + A[0]],
                          [A[1] * 10 + A[3], A[0] * 10 + A[2]],
                          [A[1] * 10 + A[3], A[2] * 10 + A[0]],

                          [A[2] * 10 + A[1], A[0] * 10 + A[3]],
                          [A[2] * 10 + A[1], A[3] * 10 + A[0]],
                          [A[2] * 10 + A[0], A[1] * 10 + A[3]],
                          [A[2] * 10 + A[0], A[3] * 10 + A[1]],
                          [A[2] * 10 + A[3], A[1] * 10 + A[0]],
                          [A[2] * 10 + A[3], A[0] * 10 + A[1]],

                          [A[3] * 10 + A[1], A[2] * 10 + A[0]],
                          [A[3] * 10 + A[1], A[0] * 10 + A[2]],
                          [A[3] * 10 + A[2], A[1] * 10 + A[0]],
                          [A[3] * 10 + A[2], A[0] * 10 + A[1]],
                          [A[3] * 10 + A[0], A[1] * 10 + A[2]],
                          [A[3] * 10 + A[0], A[2] * 10 + A[1]]]

        result = [-1, -1]
        for each in possible_times:
            if 0 <= each[0] <= 23 and 0 <= each[1] <= 59:
                if each[0] > result[0] or (each[0] == result[0] and each[1] > result[1]):
                    result = each

        return "" if result == [-1, -1] else str(result[0]).zfill(2) + ':' + str(result[1]).zfill(2)