class Solution:
    def trailingZeroes(self, n: int) -> int:
        

        #We are finding the number of factors divisible by 5 in n! We don't need 2 because 5s are always less than 2. 5 is the limiting factor. In other words we are dividing n by 5, then 25 and so on until quotient is less than = n to get the number 

        #example : look 6!
        # 6 * 5 * 4 * 3 * 2 * 1 

        quotient = 5
        zeros = 0
        while quotient<=n:
            t = n // quotient
            zeros+=t
            quotient = quotient*5
        return zeros
            
            