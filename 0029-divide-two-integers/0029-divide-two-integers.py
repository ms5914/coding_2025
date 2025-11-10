class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        

          # Constants.
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        num_negatives = 0
        if dividend < 0:
            num_negatives+=1
        if divisor < 0:
            num_negatives+=1
        
        dividend = -dividend if dividend > 0 else dividend
        divisor = -divisor if divisor > 0 else divisor
        
        key = divisor
        count = 0
        while dividend<=key:
            times = 1
            while dividend <= key+key and key>pow(-2, 31)//2:
                times+=times
                key += key
            dividend -= key
            key = divisor
            count += times
        
        if num_negatives == 1:
            return -count
        else:
            return count
        
        
        
        
        
        
        
            
            
            
            
        
        