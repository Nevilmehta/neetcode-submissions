class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for a,b in intervals:

            # no overlap
            if not res or a>res[-1][1]:
                res.append([a,b])

            # overlap
            else:
                res[-1][1] = max(res[-1][1], b)

        return res