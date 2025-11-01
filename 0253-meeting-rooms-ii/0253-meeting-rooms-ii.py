class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        starts = [start for start, _ in intervals]
        ends = [end for _, end in intervals]
        
        starts.sort()
        ends.sort()
        
        i, j = 0, 0
        
        count = 0
        max_count = 0
        while i<len(starts) and j<len(ends):
            if starts[i] < ends[j]:
                count+=1
                max_count = max(count, max_count)
                i+=1
            else:
                count-=1
                j+=1
                
        return max_count
        
                
            
        
        
        