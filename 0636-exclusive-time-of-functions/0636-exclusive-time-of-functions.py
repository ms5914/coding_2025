class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        st = []
        duration = [0 for i in range(n)]

        for log in logs:
            splits = log.split(":")
            
            function = splits[0]
            op = splits[1]
            time = splits[2]

            if op == "end":
                if st and st[-1][0] == function:
                    top = st.pop()
                    duration[int(function)]+=int(time)-int(top[2])+1

                    if st and st[-1][1] == "start":
                        duration[int(st[-1][0])]-=int(time)-int(top[2])+1
            else:
                st.append(splits)
        
        return duration
                    


        