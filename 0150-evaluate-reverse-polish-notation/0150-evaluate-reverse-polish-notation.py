class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operations = {
            "+": lambda a, b: a+b, 
            "-": lambda a, b: a-b,
            "*": lambda a, b: a*b,
            "/": lambda a, b: int(a/b)
        }

        for token in tokens:
            if token in operations.keys():
                operator = operations[token]
                second = st.pop()
                first = st.pop()
                st.append(operator(first, second))
            else:
                st.append(int(token))
        
        return st[0]
        