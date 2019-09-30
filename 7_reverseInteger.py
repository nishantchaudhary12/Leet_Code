'''Given a 32-bit signed integer, reverse digits of an integer.'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 2147483647 and x >= -2147483648:
            flag = False
            if x < 0:
                flag = True
            x = abs(x)
            result = 0
            while x != 0:
                result = result * 10 + x % 10
                x = x // 10
            if result <= 2147483647 and result >= -2147483648:
                if flag:
                    result = -result
                else:
                    result = result
            else:
                result = 0
        else:
            result = 0
        return result