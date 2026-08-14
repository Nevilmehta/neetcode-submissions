class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x:x[1])

        end = intervals[0][1]
        for i in range(1, len(intervals)):
            # overlap
            if intervals[i][0]<end:
                count+=1
            # non overlap
            else:
                end = intervals[i][1]

        return count