class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        subset = []

        def backtrack(start, total):
            if total == target:
                res.append(subset[:])
                return

            if total>target:
                return 

            for i in range(start, len(candidates)):
                # only difference is to skip duplicates choice at the same level
                if i>start and candidates[i]==candidates[i-1]:
                    continue

                subset.append(candidates[i])
                # i+1 because each number can be used only once
                backtrack(i+1, total+candidates[i])
                subset.pop()

        backtrack(0,0)
        return res

