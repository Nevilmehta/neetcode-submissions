class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(start, total):

            # if found valid combination
            if total==target:
                res.append(subset[:])
                return

            # we went over target
            if total>target:
                return 

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i, total+nums[i])
                subset.pop()

        backtrack(0,0)

        return res
