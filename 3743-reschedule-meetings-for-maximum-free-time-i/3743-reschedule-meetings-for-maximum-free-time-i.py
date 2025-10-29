class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
     
        
        window_size = 0
        max_free = 0
        n = len(startTime)
        free_time, max_free = 0, 0
        for i in range(n):
            window_size+=1
            free_time += startTime[i]-endTime[i-1] if i>0 else startTime[i]
            if window_size == k:
                toadd = startTime[i+1]-endTime[i] if i<n-1 else eventTime-endTime[i]
                total_time = free_time+toadd
                max_free = max(max_free, total_time)
                window_size -=1
                free_time -= startTime[i-k+1]-endTime[i-k] if i-k+1>0 else startTime[i-k+1]
        return max_free

            
        