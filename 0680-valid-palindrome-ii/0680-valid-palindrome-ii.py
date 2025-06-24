class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<=1:
            return True

        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return s[i+1:len(s)-i]==s[i+1:len(s)-i][::-1] or s[i:len(s)-i-1] == s[i:len(s)-i-1][::-1]
        
        return True
        