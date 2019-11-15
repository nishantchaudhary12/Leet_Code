'''The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.'''


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = '{0:032b}'.format(x)
        y = '{0:032b}'.format(y)
        i = 0
        count = 0
        while i < 32:
            if x[i] != y[i]:
                count += 1
            i += 1
        return count