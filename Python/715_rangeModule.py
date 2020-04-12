'''A Range Module is a module that tracks ranges of numbers. Your task is to design and
implement the following interfaces in an efficient manner.

addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval.
Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval
[left, right) that are not already tracked.
queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right) is currently being tracked.
removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval [left, right).'''

import bisect

class RangeModule:

    def __init__(self):
        self.range = list()

    def _helper(self, left, right):
        i = 0
        j = len(self.range) - 1
        for k in (100, 10, 1):
            while i + k - 1 < len(self.range) and self.range[i + k - 1][1] < left:
                i += k
            while j >= k - 1 and self.range[j - k + 1][0] > right:
                j -= k
        return i, j

    def addRange(self, left: int, right: int) -> None:
        i, j = self._helper(left, right)
        if i <= j:
            left = min(left, self.range[i][0])
            right = max(right, self.range[j][1])
        self.range[i:j + 1] = [(left, right)]

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_left(self.range, (left, 2 ** 31))
        if i:
            i = i - 1
        if self.range:
            if self.range[i][0] <= left and self.range[i][1] >= right:
                return True

    def removeRange(self, left: int, right: int) -> None:
        i, j = self._helper(left, right)
        new = list()
        for k in range(i, j + 1):
            if self.range[k][0] < left:
                new.append((self.range[k][0], left))
            if right < self.range[k][1]:
                new.append((right, self.range[k][1]))
        self.range[i:j + 1] = new

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)