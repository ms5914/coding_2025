class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
             #The idea is that 1. the k events that we should move should always be contiguous, and so this 
        # becomes a sliding window problem where we assume that we will compress together the contiguous k events (we don't need to consider less than k events) and then find out the empty space  
        # after every k size window(the empty space will be the summation of space before first event + space between first and second event + space between second and third and so + space between kth and k-th event and in the space between kth and kth+1 event (this will be calculated via toadd variable))
        #then just slide the window, i.e decrement the window size by 1, remove the i-kth space that we had previously added
        #the answer is the max_free time that we can get via all such windows  
        
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

            
        