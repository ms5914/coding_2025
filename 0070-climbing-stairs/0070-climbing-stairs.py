class Solution:
    def climbStairs(self, n: int) -> int:
        
        num_ways = [0 for i in range(n+1)]
        num_ways[0] = 1
        num_ways[1] = 1
        
        for i in range(2, n+1):
            num_ways[i] = num_ways[i-1] + num_ways[i-2]
        
        return num_ways[n]
        