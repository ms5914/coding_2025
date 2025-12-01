class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_len(low, high):
            ans = 0
            while low>=0 and high<len(s) and s[low]==s[high]:
                ans+=1
                low-=1
                high+=1
            return ans

        ans = 0
        for i in range(len(s)):
            ans+=count_len(i, i+1)
            ans+=count_len(i, i)
        return ans
            
        