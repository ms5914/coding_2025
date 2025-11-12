class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_map = defaultdict(int)
        max_count = 0
        max_count_letter_count = 0
        
        for task in tasks:
            count_map[task]+=1
            if count_map[task] > max_count:
                max_count = count_map[task]
                max_count_letter_count=1
            elif count_map[task] == max_count:
                max_count_letter_count+=1
        
        empty_slots = n * (max_count-1)
        empty_slots_updated = max(0, empty_slots - ((max_count-1)*(max_count_letter_count-1)))
        tasks_yet_to_be_assigned = len(tasks)- (max_count*max_count_letter_count)
        empty_slots = max(0, empty_slots_updated-tasks_yet_to_be_assigned)

        return len(tasks)+empty_slots
            
            
        