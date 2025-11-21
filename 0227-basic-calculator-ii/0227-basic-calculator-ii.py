class Solution:
    def calculate(self, s: str) -> int:
        s = s + "$"
        prev_num = 0
        curr_num = 0
        prev_sign = "+"
        result = 0
        i = 0
        for ch in s:
            print(ch)
            if ch.isdigit():
                curr_num = curr_num*10+int(ch)
            elif ch in "+-*/$" :
                if prev_sign in "+-":
                    result+=prev_num
                    prev_num = curr_num if prev_sign == "+" else -curr_num
                elif prev_sign == "*":
                    prev_num = prev_num*curr_num
                elif prev_sign == "/":
                    prev_num = int(prev_num/curr_num)
                curr_num = 0
                prev_sign = ch

            i+=1
        
        return result+prev_num
                


         