"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        scheduled = set()
        rooms = 0

        while len(scheduled) < len(intervals):
            rooms += 1
            i = 0
            while i in scheduled:
                i += 1
            scheduled.add(i)
            prevEnd = intervals[i].end

            while i < len(intervals):
                if i not in scheduled and intervals[i].start >= prevEnd:
                    scheduled.add(i)
                    prevEnd = intervals[i].end
                i += 1
            
            print(scheduled)
        
        return rooms