class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        negative = False
        res = 0
        i = 0
        
        if not s:
            return 0
        
        if s[i] in ('-', '+'):
            negative = True if s[i] == '-' else False
            i+=1
            
        while i<len(s) and s[i] == 0:
            i+=1
            
        while i<len(s) and s[i].isdigit():
            if res*10 >= pow(2, 31):
                if negative:
                    return -1*pow(2,31)
                else:
                    return pow(2,31)-1

            res = res*10+int(s[i])
            i+=1
        
        if res >= pow(2, 31):
            if negative:
                return -1*pow(2,31)
            else:
                return pow(2,31)-1
        else:
            return -1*res if negative else res
            
            
            
            
        
        