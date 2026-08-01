class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def can(k):
            hours = 0
            for p in piles:
                hours += (p + k - 1)//k
            return hours<=h

        while left<=right:
            mid = (left + right)//2
            if can(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left