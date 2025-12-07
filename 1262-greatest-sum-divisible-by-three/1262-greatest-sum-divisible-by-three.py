class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        prev = [0, float('-inf'), float('-inf')]
        for i in range(len(nums)):
            num = nums[i]
            new = [0 for i in range(3)]
            for r in range(3):
                exclude_num = prev[r]
                prev_remainder = (r - num) % 3
                include_num = prev[prev_remainder] + num
                new[r] = max(exclude_num, include_num)
            prev = new
        return new[0]

# class Solution:
#     def maxSumDivThree(self, nums: List[int]) -> int:
#         dp = [[0  for j in range(3)] for i in range(len(nums)+1)]
#         for i in range(1, len(nums)+1):
#             dp[i] = dp[i-1][:]
#             for j in dp[i-1]:
#                 dp[i][(j+nums[i-1])%3] = max(dp[i][(j+nums[i-1])%3], j+nums[i-1])
#         return dp[len(nums)][0]


# def maxSumDivThree(self, nums: List[int]) -> int:
# 	n = len(nums)
# 	dp = [[0]*3 for _ in range(n+1)]
# 	dp[0][1] = float('-inf')
# 	dp[0][2] = float('-inf')
# 	for i in range(1, n+1):
# 		if nums[i-1] % 3 == 0: # Current remainder == 0
# 			dp[i][0] = max(dp[i-1][0], dp[i-1][0] + nums[i-1]) # Current remainder is 0, so we add to dp[i-1][0] to keep the remainder 0
# 			dp[i][1] = max(dp[i-1][1], dp[i-1][1] + nums[i-1]) # Current remainder is 0, so we add to dp[i-1][1] to keep the remainder 1
# 			dp[i][2] = max(dp[i-1][2], dp[i-1][2] + nums[i-1]) # Current remainder is 0, so we add to dp[i-1][2] to keep the remainder 2
# 		elif nums[i-1] % 3 == 1: # Current remainder == 1
# 			dp[i][0] = max(dp[i-1][0], dp[i-1][2] + nums[i-1]) # Current remainder is 1, so we add to dp[i-1][2] to keep the remainder 0
# 			dp[i][1] = max(dp[i-1][1], dp[i-1][0] + nums[i-1]) # Current remainder is 1, so we add to dp[i-1][0] to keep the remainder 1
# 			dp[i][2] = max(dp[i-1][2], dp[i-1][1] + nums[i-1]) # Current remainder is 1, so we add to dp[i-1][1] to keep the remainder 2
# 		else: # Current remainder == 2
# 			dp[i][0] = max(dp[i-1][0], dp[i-1][1] + nums[i-1]) # Can you tell how this works now?
# 			dp[i][1] = max(dp[i-1][1], dp[i-1][2] + nums[i-1])
# 			dp[i][2] = max(dp[i-1][2], dp[i-1][0] + nums[i-1])

# 	return dp[-1][0]


















         