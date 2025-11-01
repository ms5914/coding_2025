class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest,i = 0,0
        while i<=farthest and i<len(nums):
            farthest = max(farthest, nums[i]+i)
            if farthest >= len(nums)-1:
                return True
            i+=1
        return False
        
        