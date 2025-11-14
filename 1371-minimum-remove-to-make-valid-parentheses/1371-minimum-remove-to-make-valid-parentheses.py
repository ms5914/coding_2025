class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        indexes_to_remove = set()
        for i, ch in enumerate(s):
            if ch == "(":
                st.append((ch, i))
            elif ch == ")":
                if st and st[-1][0] == "(":
                    st.pop()
                else:
                    indexes_to_remove.add(i)
        
        for ch, i in st:
            indexes_to_remove.add(i)
        
        result = []
        for i,ch in enumerate(s):
            if not i in indexes_to_remove:
                result.append(ch)
        
        return "".join(result)



        
        


        