'''Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.'''

import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort()
        rooms = [intervals[0][1]]
        # count = 1
        for i in range(1, len(intervals)):
            if not rooms:
                heapq.heappush(each[1])
                # count += 1
            else:
                curr = rooms[0]
                if curr <= intervals[i][0]:
                    # count += 1
                    # else:
                    heapq.heappop(rooms)
                heapq.heappush(rooms, intervals[i][1])

        # return count
        return len(rooms)