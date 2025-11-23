class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        st = []

        for i in range(len(heights)):
            while st and heights[st[-1]]<=heights[i]:
                st.pop()
            st.append(i)
        
        return st
        