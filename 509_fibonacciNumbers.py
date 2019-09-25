#fibonacci numbers
'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1.
'''

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 1
        i = 0
        j = 1
        if N == 0:
            return 0
        else:
            while count != N:
                temp = i + j
                i = j
                j = temp
                count += 1
            return j