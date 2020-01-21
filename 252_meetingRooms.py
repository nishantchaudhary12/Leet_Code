'''Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.'''


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals: return True
        intervals.sort()
        lastMeeting = intervals[0][1]
        for i in range(1, len(intervals)):
            if lastMeeting > intervals[i][0]:
                return False
            else:
                lastMeeting = intervals[i][1]
        return True