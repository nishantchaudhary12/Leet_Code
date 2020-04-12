'''Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.'''


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i] % 2 != 0:
                while A[j] % 2 != 0 and i < j:
                    j -= 1
                    if j == -1:
                        break
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            else:
                i += 1
        return A
