'''Implement pow(x, n), which calculates x raised to the power n (xn).'''


class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x == 1 or n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        even = x
        odd = 1
        while n != 1:
            if n % 2 == 0:
                even *= even
                n /= 2
            else:
                odd *= even
                n -= 1

        return even * odd