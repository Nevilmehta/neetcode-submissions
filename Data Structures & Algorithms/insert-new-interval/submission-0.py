class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval

        left = []
        right = []

        for a,b in intervals:
            if b<s:
                left.append([a,b])

            elif a>e:
                right.append([a,b])

            else:
                s = min(s,a)
                e = max(e,b)

        return left + [[s,e]] + right
