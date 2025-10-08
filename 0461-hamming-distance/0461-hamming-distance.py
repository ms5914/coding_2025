class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y
        
        if not a:
            return 0
        
        count = 0
        while a>0:
            a = a&a-1
            count+=1
            
        return count
        