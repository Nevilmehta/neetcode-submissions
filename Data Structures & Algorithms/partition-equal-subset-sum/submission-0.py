class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
    
        # If total sum is odd, we cannot partition into equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(nums)

        # Initialize the DP array
        dp = [False] * (target + 1)
        dp[0] = True  # Zero sum is always possible with empty subset

        for num in nums:
            for t in range(target, num - 1, -1):  # Reverse to avoid overwriting
                dp[t] = dp[t] or dp[t - num]

        return dp[target]