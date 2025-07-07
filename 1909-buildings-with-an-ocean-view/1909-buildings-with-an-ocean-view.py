class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        st = []
        for i, height in enumerate(heights):
            while st and heights[st[-1]]<=height:
                st.pop()
            st.append(i)
        return st
        