class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next_number(n):
            sum_res = 0
            while n:
                n, remainder = divmod(n, 10)
                sum_res += remainder**2
            return sum_res
        
        slow_ptr, fast_pointer = n, get_next_number(n)

        while slow_ptr != fast_pointer and fast_pointer !=1:
            slow_ptr = get_next_number(slow_ptr)
            fast_pointer = get_next_number(get_next_number(fast_pointer))
        
        return fast_pointer == 1


