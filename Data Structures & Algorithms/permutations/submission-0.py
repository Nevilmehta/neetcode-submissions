class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack():

            if len(subset) == len(nums):
                res.append(subset[:])
                return 

            for num in nums:
                if num in subset:
                    continue

                subset.append(num)
                backtrack()
                subset.pop()

        backtrack()

        return res