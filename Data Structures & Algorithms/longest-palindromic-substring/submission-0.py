class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[False]*n for _ in range(n)]
        longest = ""

        for r in range(n):
            for l in range(r, -1, -1):

                if s[l] == s[r] and (r-l<=2 or dp[l+1][r-1]):
                    dp[l][r] = True

                    if r-l+1 > len(longest):
                        longest = s[l:r+1]

        return longest