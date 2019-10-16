'''Given an integer (signed 32 bits), write a function to check whether it is a power of 4.'''


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        else:
            curr = 4
            i = 2
            while curr < num:
                curr = 4 ** i
                i += 1
            if curr == num:
                return True
            return False
