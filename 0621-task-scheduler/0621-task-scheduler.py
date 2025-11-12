class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_map = defaultdict(int)
        
        #max count
        max_count = 0

        #no of letters with max count
        max_count_letter_count = 0
        
        for task in tasks:
            count_map[task]+=1
            if count_map[task] > max_count:
                max_count = count_map[task]
                max_count_letter_count=1
            elif count_map[task] == max_count:
                max_count_letter_count+=1
        
        empty_slots = n * (max_count-1)
        
        # For max frequency elements only max_freq-1 elements can fill empty spots, 1 of each of     those  will be added towards the end. Empty slots can't be negative, because rest of the elements can be plugged in between. 

        empty_slots_updated = max(0, empty_slots - ((max_count-1)*(max_count_letter_count-1)))
        
        #max freq elements are already taken into account via empty_slots_updated
        tasks_yet_to_be_assigned = len(tasks)- (max_count*max_count_letter_count)

        #final empty slots
        empty_slots = max(0, empty_slots_updated-tasks_yet_to_be_assigned)

        return len(tasks)+empty_slots
        