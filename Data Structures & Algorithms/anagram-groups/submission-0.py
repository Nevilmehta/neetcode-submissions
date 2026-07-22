class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for word in strs:
            key = "".join(sorted(word))
            
            res[key].append(word)

        return [value for value in list(res.values())]