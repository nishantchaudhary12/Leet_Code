'''Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        result = list()
        indx = 0
        start = newInterval[0]
        end = newInterval[1]
        while indx < len(intervals) and start > intervals[indx][0]:
            result.append(intervals[indx])
            indx += 1

        if not result or result[-1][-1] < start:
            result.append(newInterval)
        else:
            result[-1][-1] = max(result[-1][-1], end)

        while indx < len(intervals):
            if result[-1][-1] < intervals[indx][0]:
                result.append(intervals[indx])
            else:
                result[-1][-1] = max(result[-1][-1], intervals[indx][1])
            indx += 1
        return result