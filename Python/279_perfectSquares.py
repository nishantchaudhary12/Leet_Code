'''Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.'''


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        perfect_num_list = list()
        while i * i <= n:
            perfect_num_list.append(i*i)
            i += 1
        curr_count = 0
        num = {n}
        while num:
            curr_count += 1
            newSet = set()
            for i in num:
                for j in perfect_num_list:
                    if i == j:
                        return curr_count
                    elif j < i:
                        newSet.add(i - j)
                    else:
                        break
            num = newSet