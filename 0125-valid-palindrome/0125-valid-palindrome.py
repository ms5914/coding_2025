class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     res = []
    #     for ch in s:
    #         if ch.isalnum():
    #             res.append(ch.lower())
        
        
    #     def isPal(res):
    #         low = 0
    #         high = len(res)-1
            
    #         while low<high:
    #             if res[low] != res[high]:
    #                 return False
    #             low+=1
    #             high-=1
    #         return True
        
    #     return isPal(res)

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if left < right and s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
        