class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(i, j, s):
            max_len = 0
            while i>=0 and j<len(s) and s[i] == s[j]:
                max_len = j-i+1
                i-=1
                j+=1
                
            return (max_len, i+1, j-1) 
        
        
        
        max_str = ""
        max_len = 0
        start = 0
        end = 0
        
        for i in range(len(s)):
            max_len_1, i1,j1 = expand(i, i+1, s)
            max_len_2, i2, j2 = expand(i, i, s)
            if max_len_1>max_len_2:
                max_i = i1
                max_j = j1
            else:
                max_i = i2
                max_j = j2
            
            if max_j-max_i+1 > max_len:
                start = max_i
                end = max_j
                max_len = max_j-max_i+1
        
        return s[start:end+1]
            
                
            
            
            
            
            
            
            
            
            
        