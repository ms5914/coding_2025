class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            self.find_two_sum(nums[i], i+1, len(nums)-1, nums, res)
        return res
        
    def find_two_sum(self, target, start, end, nums, res):
        while start<end:
            if nums[start]+nums[end] == -1*target:
                res.append([nums[start], nums[end], target])
                start+=1
                end-=1
                while start<end and nums[start] == nums[start-1]:
                    start+=1
                while start<end and nums[end] == nums[end+1]:
                    end-=1
            elif nums[start]+nums[end] < -1*target:
                start+=1
                while start<end and nums[start] == nums[start-1]:
                    start+=1
            else:
                end-=1
                while start<end and nums[end] == nums[end+1]:
                    end-=1


                
        
        
            [-4, -1, -1, 0, 1, 2 ]