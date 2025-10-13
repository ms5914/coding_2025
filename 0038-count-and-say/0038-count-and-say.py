class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"
        
        def say(s):
            prev = s[0]
            count = 1
            li = []
            for ch in s[1:]:
                if ch == prev:
                    count+=1
                else:
                    li.append(str(count))
                    li.append(prev)
                    prev = ch
                    count = 1
            li.append(str(count))
            li.append(prev)
            return "".join(li)
        
        prev_str = "1"
        for i in range(1, n): 
            res = say(prev_str)
            prev_str = res
        return res
        
        
        

                
                    
                