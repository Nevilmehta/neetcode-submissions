class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]*n
        right = [1]*n
        ans = [1]*n

        # for left products
        left[0] = 1
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]

        # for right products
        right[n-1] = 1
        for i in range(n-2,-1, -1):
            right[i] = right[i+1]*nums[i+1]

        # final answer
        for i in range(n):
            ans[i] = left[i]*right[i]

        return ans