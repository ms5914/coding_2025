class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # 1. Initialize with -inf for remainders 1 and 2 (impossible for sum 0)
        #    Only remainder 0 is possible with 0 elements (sum 0).
        dp = [[0, float('-inf'), float('-inf')] for _ in range(len(nums) + 1)]
        
        for i in range(1, len(nums) + 1):
            # REMOVED: dp[i] = dp[i-1][:] 
            
            num = nums[i-1]
            for r in range(3):
                # 2. Logic Update:
                # Compare excluding the number (dp[i-1][r]) 
                # vs including the number (dp[i-1][prev_remainder] + num)
                
                exclude_num = dp[i-1][r]
                
                # Calculate which previous remainder would result in current remainder 'r' if we add 'num'
                prev_remainder = (r - num) % 3
                include_num = dp[i-1][prev_remainder] + num
                
                dp[i][r] = max(exclude_num, include_num)
                
        return dp[len(nums)][0]