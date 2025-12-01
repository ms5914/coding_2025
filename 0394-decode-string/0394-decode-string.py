class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        result = []
        while i < len(s):
            open_count = 0
            num = 0
            internal_li = []
            first_str = []

            while i<len(s) and not s[i].isdigit():
                first_str.append(s[i])
                i+=1
            result.append("".join(first_str))

            while i<len(s) and s[i].isdigit():
                num = num*10+int(s[i])
                i+=1
            i+=1
            open_count+=1
            while open_count != 0 and i<len(s):
                internal_li.append(s[i])
                if s[i] == "[":
                    open_count+=1
                elif s[i] == "]":
                    open_count-=1
                i+=1
            
            decoded_result = self.decodeString("".join(internal_li[:-1]))
            for k in range(num):
                result.append(decoded_result)
        return "".join(result)
            
                
                


            


            


        