class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p)>len(s):
            return []

        dict_p = Counter(p)
        dict_s = defaultdict(int)
        i = 0
        j = 0 
        result = []
        while j<len(s):
            dict_s[s[j]]+=1
            if j-i+1 == len(p):
                if dict_p == dict_s:
                    result.append(i)
                dict_s[s[i]]-=1
                if dict_s[s[i]] == 0:
                    del dict_s[s[i]]
                i+=1
            j+=1
        return result


