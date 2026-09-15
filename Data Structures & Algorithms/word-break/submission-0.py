class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)

        dp = [False]*(len(s)+1)
        dp[len(s)] = True


        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordset and dp[j]:
                    dp[i] = True
                    break

        return dp[0]