class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = [0 for i in range(26)]
        for ch in s:
            counter[ord(ch)-ord('a')] += 1
        
        for i, ch in enumerate(s):
            if counter[ord(ch)-ord('a')] ==1:
                return i
        return -1
        
        