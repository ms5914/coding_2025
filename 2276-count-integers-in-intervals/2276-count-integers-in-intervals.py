"""
bisect_left returns an insertion index in a sorted array to the left of the search value. 
bisect_right returns an insertion index in a sorted array to the right of the search value. 
See the python documentation for more details. 
"""
class CountIntervals:

    def __init__(self):
        self.intervals = []
        self.count_of_integers = 0

    def add(self, left: int, right: int) -> None:
        # To make the interval inclusive of right
        right += 1
        
        # Find positions to insert the new interval
        start_index = bisect_left(self.intervals, left)
        end_index = bisect_right(self.intervals, right)

        # Adjust the left boundary if overlapping with an existing interval
        if start_index % 2 == 1:
            left = self.intervals[start_index - 1]
            start_index -= 1
            
        # Adjust the right boundary if overlapping with an existing interval
        if end_index % 2 == 1:
            right = self.intervals[end_index]
            end_index += 1
            
        # Remove the length of all intervals that will be merged
        for i in range(start_index, end_index, 2):
            self.count_of_integers -= self.intervals[i + 1] - self.intervals[i]        
        
        # Add the length of the new merged interval
        self.count_of_integers += right - left
        
        # Update the list of intervals
        self.intervals[start_index:end_index] = [left, right]
        
    def count(self) -> int:
        return self.count_of_integers