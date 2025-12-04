class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums)==1:
            return 0
        farthest,i, nextfarthest = nums[0],1,nums[0]
        jumps=1
        while i<=farthest and i<len(nums):
            nextfarthest = max(nextfarthest, nums[i]+i)
            if farthest >= len(nums)-1:
                return jumps
            if i == farthest:
                print(i)
                farthest = nextfarthest
                jumps+=1
            i+=1
        