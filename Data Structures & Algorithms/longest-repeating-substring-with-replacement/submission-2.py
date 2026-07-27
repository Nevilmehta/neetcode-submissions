class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0)+1
            max_len = max(max_len, count[s[right]])
            if (right - left + 1) - max_len>k:
                count[s[left]]-=1
                left+=1

        return len(s)-left