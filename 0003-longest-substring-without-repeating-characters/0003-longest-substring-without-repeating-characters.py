class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        i = 0
        char_index = {}
        char_index[s[i]] = i
        max_len = 1
        
        for j in range(1, len(s)):
            if not s[j] in char_index:
                max_len = max(max_len, j-i+1)
                char_index[s[j]] = j
            else:
                i = max(i, char_index[s[j]]+1)
                max_len = max(max_len, j-i+1)
                char_index[s[j]] = j
        return max_len
            
                
                
            
        