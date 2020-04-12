'''You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.'''


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        while sticks:
            first = heapq.heappop(sticks)
            if sticks:
                second = heapq.heappop(sticks)
                curr = first + second
                cost += curr
                heapq.heappush(sticks, curr)
        return cost