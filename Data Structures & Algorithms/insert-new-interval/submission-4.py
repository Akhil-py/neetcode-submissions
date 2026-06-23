class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        fixedIntervals = []
        k = 0
        while k < len(intervals) and newInterval[0] >= intervals[k][0]:
            k += 1
            print(k)
        intervals.insert(k, newInterval)
        print(intervals)

        fixedIntervals.append(intervals[0])

        for i in intervals:
            if i[0] > fixedIntervals[-1][1]:
                fixedIntervals.append(i)
            elif i[1] > fixedIntervals[-1][1]:
                fixedIntervals[-1][1] = i[1]

        return fixedIntervals