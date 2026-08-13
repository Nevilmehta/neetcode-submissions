class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        subset = []

        def backtrack(i):
            # we used every digit
            if i == len(digits):
                res.append("".join(subset))
                return 

            # get letters for current digit
            chars = letters[digits[i]]

            for char in chars:
                subset.append(char)
                backtrack(i+1)
                subset.pop()

        backtrack(0)

        return res