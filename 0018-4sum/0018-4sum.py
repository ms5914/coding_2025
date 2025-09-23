class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.ksum(4, 0, len(nums)-1, nums, target)
    


    def ksum(self, k, start, end, nums, target):
        if k == 2:
            return self.find_two_sum(target, start, end, nums)
        else:
            result = []
            for i in range(start, end+1):
                if i>start and nums[i] == nums[i-1]:
                    continue
                for subset in self.ksum(k-1, i+1, end, nums, target-nums[i]):
                    result.append([nums[i]]+subset)
            
            return result 

    def find_two_sum(self, target, start, end, nums):
        res = []
        while start<end:
            if nums[start]+nums[end] == target:
                res.append([nums[start], nums[end]])
                start+=1
                end-=1
                while start<end and nums[start] == nums[start-1]:
                    start+=1
                while start<end and nums[end] == nums[end+1]:
                    end-=1
            elif nums[start]+nums[end] < target:
                start+=1
                while start<end and nums[start] == nums[start-1]:
                    start+=1
            else:
                end-=1
                while start<end and nums[end] == nums[end+1]:
                    end-=1
        return res
        