class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n<0:
            n = -1*n
            x = 1.0/x
        result = 1
        while n>0:
            if n%2 == 1:
                n = n-1
                result = result*x
    
            n = n//2
            x = x*x
        return result

        