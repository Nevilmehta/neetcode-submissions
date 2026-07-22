class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        res = []

        # count freq
        for num in nums:
            freq[num] = freq.get(num, 0)+1

        # sort the freq
        sorted_freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)

        # take first k elements
        for i in range(k):
            res.append(sorted_freq[i][0])

        return res