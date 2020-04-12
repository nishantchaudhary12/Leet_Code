'''Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        num = 0
        res = list()
        while i >= 0 or j >= 0:
            first = (ord(num1[i]) - 48) if i > - 1 else 0
            second = (ord(num2[j]) - 48) if j > - 1 else 0
            curr = first + second + carry
            # print(curr)
            if curr > 9:
                carry = 1
                curr %= 10
            else:
                carry = 0

            res.append(str(curr))

            i -= 1
            j -= 1
        if carry: res.append('1')
        return ''.join(res[::-1])