class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = deque()
        res = []
        for i in range(len(nums)):
            # remove indices outside window
            while q and q[0]<=i-k:
                q.popleft()

            # remove smaller element
            while q and nums[q[-1]]<nums[i]:
                q.pop()

            # add
            q.append(i)

            # if window is complete
            if i>=k-1:
                res.append(nums[q[0]])

        return res
