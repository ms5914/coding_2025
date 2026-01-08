class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [-1]
        max_area = 0
        for i in range(len(heights)):
            while st[-1] != -1 and heights[st[-1]]>heights[i]:
                curr_height = heights[st.pop()]
                prev_index = st[-1]
                curr_width = i-prev_index-1
                max_area = max(max_area, curr_height*curr_width)
            st.append(i)

        while st[-1] != -1:
            index = st.pop()
            curr_height = heights[index]
            curr_width = len(heights)-st[-1]-1
            max_area = max(max_area, curr_width*curr_height)
        return max_area



    


    
        