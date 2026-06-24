class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        mergedIntervals = []
        mergedIntervals.append(intervals[0])

        for i in intervals:
            if i[0] > mergedIntervals[-1][1]:
                mergedIntervals.append(i)
            elif i[1] > mergedIntervals[-1][1]:
                mergedIntervals[-1][1] = i[1]
        
        return mergedIntervals
