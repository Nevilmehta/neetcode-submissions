class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        n = len(s)
        one = 1
        two = 1

        for i in range(n - 1, -1, -1):
            temp = one

            if s[i] == "0":
                one = 0

            elif i + 1 < n and "10" <= s[i:i+2] <= "26":
                one += two

            two = temp

        return one