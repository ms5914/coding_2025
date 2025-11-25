class Solution:
    def maximumSwap(self, num: int) -> int:

        num_str = list(str(num))
        left, right = -1, -1
        max_so_far = num_str[-1]
        max_so_far_index = len(num_str)-1
        
        for i in range(len(num_str)-2, -1, -1):
            if num_str[i]>max_so_far:
                max_so_far = num_str[i]
                max_so_far_index = i
            elif num_str[i]<max_so_far:
                left = i
                right = max_so_far_index
        
        if left !=-1 and right!=-1:
            temp = num_str[left]
            num_str[left] = num_str[right]
            num_str[right] = temp
            return int("".join(num_str))
        
        else:
            return num
            