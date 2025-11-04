class Solution:
    def isHappy(self, n: int) -> bool:
        
        def square_sum(p):
            t = 0
            while p>0:
                num = p%10
                t = t+pow(num,2)
                p = p//10
            return t
        
        s = set()
        while n not in s:
            s.add(n)
            n = square_sum(n)
            if n == 1:
                return True
            
            
        return False
        
    
    
        
        