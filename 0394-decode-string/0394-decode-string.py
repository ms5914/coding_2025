class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        def decode(s):
            result = []
            nonlocal i
            while i < len(s) and s[i] !="]":
                if i<len(s) and not s[i].isdigit():
                    result.append(s[i])
                    i+=1
                else:
                    num = 0
                    while i<len(s) and s[i].isdigit():
                        num = num*10+int(s[i])
                        i+=1
                    i+=1
                    
                    result_str = decode(s)

                    i+=1

                    for k in range(num):
                        result.append(result_str)
                
            return "".join(result)

        return decode(s)
                




        # st = []
        # i = 0
        # while i < len(s):
        #     if s[i] == "]":
        #         inside_list = []
        #         while st and st[-1] != "[":
        #             ch = st.pop()
        #             inside_list.append(ch)
        #         st.pop()
        #         inside_str = "".join(inside_list[::-1])
                
        #         number_list = []
        #         while st and st[-1].isdigit():
        #             number_list.append(st.pop())
                
        #         number = int("".join(number_list[::-1]))

        #         to_push_list = []
        #         for k in range(number):
        #             to_push_list.append(inside_str)
                
        #         st.append("".join(to_push_list))
        #     else:
        #         st.append(s[i])
        #     i+=1
        
        # return "".join(st)
        


                





        # i = 0
        # result = []
        # while i < len(s):
        #     open_count = 0
        #     num = 0
        #     internal_li = []
        #     first_str = []
        #     while i<len(s) and not s[i].isdigit():
        #         first_str.append(s[i])
        #         i+=1
        #     result.append("".join(first_str))

        #     while i<len(s) and s[i].isdigit():
        #         num = num*10+int(s[i])
        #         i+=1
        #     i+=1
        #     open_count+=1
        #     while open_count != 0 and i<len(s):
        #         internal_li.append(s[i])
        #         if s[i] == "[":
        #             open_count+=1
        #         elif s[i] == "]":
        #             open_count-=1
        #         i+=1
            
        #     decoded_result = self.decodeString("".join(internal_li[:-1]))
        #     for k in range(num):
        #         result.append(decoded_result)
        # return "".join(result)
            
                
                


            


            


        