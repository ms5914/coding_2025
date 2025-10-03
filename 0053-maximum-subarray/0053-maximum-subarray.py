class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max_sum = nums[0]
        max_so_far = nums[0]
        
        for num in nums[1:]:
            curr_max_sum = max(curr_max_sum+num, num)
            max_so_far = max(max_so_far, curr_max_sum)
            
        return max_so_far
        
        