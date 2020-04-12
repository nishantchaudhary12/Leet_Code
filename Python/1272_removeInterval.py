'''Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents the set of real numbers x such that a <= x < b.

We remove the intersections between any interval in intervals and the interval toBeRemoved.

Return a sorted list of intervals after all such removals.'''


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        intervals.sort()
        start, end = toBeRemoved[0], toBeRemoved[1]
        result = list()
        for s, e in intervals:
            if e <= start or s >= end:
                result.append([s, e])
            elif s < start and e > end:
                result.append([s, start])
                result.append([end, e])
            elif s < start and e <= end:
                result.append([s, start])
            elif s >= start and e > end:
                result.append([end, e])
        return result