class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n<0:
            n = -1*n
            x = 1.0/x
        to_multiply_in_the_end = 1
        while n>1:
            
            # every time accumulate what to multiply in the end for odd powers
            #ex: 2^9 is equal to 2^8 * (2) .. put that (2) in to_multiply_in_the_end and make the power even again by doing n = n-1
            if n%2 == 1:
                n = n-1
                to_multiply_in_the_end = to_multiply_in_the_end*x
    
            n = n//2
            x = x*x
        return to_multiply_in_the_end*x
    
    
    

        