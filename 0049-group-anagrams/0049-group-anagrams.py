class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for st in strs:
            ct = Counter(st)
            hm[tuple(sorted(ct.items()))].append(st)
        
        result = []
        print(hm)
        for val in hm.values():
            result.append(val)
        return result
            
            
        