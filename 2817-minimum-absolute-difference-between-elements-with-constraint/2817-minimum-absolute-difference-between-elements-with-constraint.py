class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        
        #think it this way, let's say you sort this array, now for each element look at all the elements at the back (on the left), you need to find those indexes that are >=x distance apart from this current number's index and get the difference (those indexes can either be greater than current number's index or less than current number's index) so you need to heaps (min for tracking min index on the left and max heap to track max index on the right) and then you keep on popping until the indexes are sufficiently apart in both (do this for both min and max heap). We pop them because for those popped indexes this current element is the only possible best solution because the rest of the incoming numbers will be greater than this current number
        
        
        
        sorted_list = [(num, i) for i, num in enumerate(nums)]
        sorted_list.sort()


        min_heap = []
        max_heap = []
        min_difference = float("inf")

        for (num, ind) in sorted_list:
            heapq.heappush(min_heap, (ind, num))
            heapq.heappush(max_heap, (-ind, num))

            while min_heap and min_heap[0][0]+x <= ind:
                min_difference = min(min_difference, num-min_heap[0][1])
                heapq.heappop(min_heap)
            
            while max_heap and -max_heap[0][0]-x >= ind:
                min_difference = min(min_difference,num-max_heap[0][1])
                heapq.heappop(max_heap)
        
        return min_difference


