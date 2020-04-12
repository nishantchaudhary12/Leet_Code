'''Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.'''


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num > 0 and num < 7:
            return True
        else:
            i = 2
            while i <= num:
                if i > 5:
                    break
                while num % i == 0:
                    num //= i
                i += 1
            if num == 1:
                return True
            else:
                return False