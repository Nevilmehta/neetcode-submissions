class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def backtrack(start):

            # we reached the end
            if start == len(s):
                res.append(subset[:])
                return

            for end in range(start, len(s)):

                # take substring
                substring = s[start:end+1]

                # only continue if its palindrome
                if substring != substring[::-1]:
                    continue

                # choose
                subset.append(substring)
                # explore
                backtrack(end+1)
                subset.pop()
        
        backtrack(0)

        return res