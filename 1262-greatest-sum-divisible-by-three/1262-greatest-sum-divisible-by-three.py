class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[0  for j in range(3)] for i in range(len(nums)+1)]

        
        for i in range(1, len(nums)+1):
            dp[i] = dp[i-1][:]
            for j in dp[i-1]:
                dp[i][(j+nums[i-1])%3] = max(dp[i][(j+nums[i-1])%3], j+nums[i-1])
        return dp[len(nums)][0]

         