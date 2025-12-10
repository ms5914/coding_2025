class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_simple(nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            
            first = nums[0]
            second = max(first, nums[1])
            
            max_profit = second
            
            for money in nums[2:]:
                curr_profit = money+first
                max_profit = max(curr_profit, max_profit)
                first = second
                second = max_profit
            return max_profit
        
        if len(nums) == 1:
                return nums[0]
            
        return max(rob_simple(nums[:-1]), rob_simple(nums[1:]))

        
        

        