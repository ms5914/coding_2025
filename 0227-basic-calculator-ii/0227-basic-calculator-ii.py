class Solution(object):
    def calculate(self, s):
        """
        """
        prev_sign = '+'
        prev = 0
        curr = 0
        result = 0

        for ch in s+'$':
            if ch in "+-/*$":
                if prev_sign == "+":
                    result = result+prev
                    prev = curr
                elif prev_sign == '-':
                    result = result+prev
                    prev = -curr
                elif prev_sign == '/':
                    prev = int(prev/float(curr))
                elif prev_sign == "*":
                    prev = prev*curr
                
                prev_sign = ch
                curr = 0
            
            elif ch.isdigit():
                curr = curr*10+int(ch)
        
        return result+prev

                
            
      



            
                
                
                


        