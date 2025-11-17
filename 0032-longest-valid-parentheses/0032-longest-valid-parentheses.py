class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        open_brackets = 0
        count=0
        for ch in s:
            if ch == "(":
                open_brackets+=1
                count+=1
            else:
                open_brackets-=1
            
            if open_brackets == 0:
                max_len = max(max_len, count*2)
            
            if open_brackets <0:
                open_brackets = 0
                count=0
        
        open_brackets = 0
        count=0
        for ch in s[::-1]:
            if ch == ")":
                open_brackets+=1
                count+=1
            else:
                open_brackets-=1
            
            if open_brackets == 0:
                max_len = max(max_len, count*2)
            
            if open_brackets < 0:
                open_brackets = 0
                count=0
        
        return max_len
        
        


        