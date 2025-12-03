class Solution:
    def reverse(self, x: int) -> int:

        sign = 1 if x>0 else -1
        x = abs(x)

        reverse = 0
        while x>0:
            x,remainder = divmod(x, 10)
            reverse = reverse*10+remainder
            if (sign > 0 and reverse > pow(2,31)-1) or (sign <0 and reverse > pow(2, 31)):
                return 0
        return sign*reverse 


        
        