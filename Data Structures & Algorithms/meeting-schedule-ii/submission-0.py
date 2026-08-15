"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        heap = []

        for interval in intervals:

            start = interval.start
            end = interval.end

            # Earliest room is free
            if heap and start >= heap[0]:
                heapq.heappop(heap)

            # Add this meeting's ending time
            heapq.heappush(heap, end)

        return len(heap)