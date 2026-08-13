class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def backtrack(open, close):

            # for all brackets
            if open==n and close==n:
                res.append("".join(subset))
                return

            # add (
            if open<n:
                subset.append("(")
                backtrack(open+1, close)
                subset.pop()

            # add )
            if close<open:
                subset.append(")")
                backtrack(open, close+1)
                subset.pop()

        backtrack(0,0)

        return res