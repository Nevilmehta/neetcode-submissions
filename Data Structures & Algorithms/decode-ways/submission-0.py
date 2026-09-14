class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        n = len(s)
        prev1, prev2 = 1, 1
        for i in range(n-1, -1, -1):
            temp=prev1
            if s[i] == "0":
                prev1 = 0
            elif i+1<n and "10"<=s[i:i+2]<="26":
                prev1 += prev2
            prev2 = temp

        return prev1