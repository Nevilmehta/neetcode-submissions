class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        count1 = {}
        count2 = {}

        # count s1
        for ch in s1:
            count1[ch]=count1.get(ch, 0)+1

        # first window
        for i in range(len(s1)):
            count2[s2[i]]=count2.get(s2[i], 0) + 1

        # Compare first window
        if count1 == count2:
            return True

        left = 0

        # sliding window
        for right in range(len(s1), len(s2)):

            # add new character
            count2[s2[right]] = count2.get(s2[right], 0)+1

            # remove old character
            count2[s2[left]] -= 1

            if count2[s2[left]] == 0:
                del count2[s2[left]]

            left+=1

            if count1 == count2:
                return True

        return False



