class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        st = []
        
        for interval in intervals:
            
            while st and st[-1][1] >= interval[0]:
                interval[0] = min(st[-1][0], interval[0])
                interval[1] = max(st[-1][1], interval[1])
                st.pop()

            st.append(interval)
        return st
            

