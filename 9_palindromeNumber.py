'''Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.'''

class Solution(object):
    def isPalindrome(self, x):
        flag = False
        original = x
        result = 0
        if x >= 0:
            while x > 0:
                result = (result * 10) + x % 10
                x = x // 10
        if result == original:
            flag = True
        return flag
