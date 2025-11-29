class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low, high = 0, 0
        char_map = {}
        len_s = len(s)
        max_len = 0
        while high < len_s:
            if  s[high] in char_map:
                low = max(low, char_map[s[high]]+1)
            max_len = max(max_len, high-low+1)     
            char_map[s[high]] = high
            high+=1
        return max_len




        
        