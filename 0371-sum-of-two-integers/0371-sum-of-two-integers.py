class Solution:
    def getSum(self, a: int, b: int) -> int:
        x = abs(a)
        y = abs(b)
        if y>x:
            return self.getSum(b, a)


        #sign of larger number    
        sign = 1 if a>=0 else -1
        

        #if addition, keep adding number and carry (adding carry is also addition)
        #keep on adding until carry becomes zero
        #xor is addition without carry
        # left shift by 1 of x&y is the carry 
        if a*b >= 0:
            while y:
                x, y = x^y, (x&y) <<1

        else:

        #if subtracting, keep subtracting number and borrow (subtracting borrow is also subtract)
        #keep on subtracting until borrow becomes zero
        #xor is subtraction without carry also
        # left shift by 1 of ~x&y is the borrow (~x&y finds positions k where x[k] is 0 and y[k] is 1 so that borrow is needed) 
            while y:
                x, y = x^y, ((~x)&y) <<1
        
        return x*sign
    