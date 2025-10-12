class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        if not nums:
            return []
        
        
        def find_two_sum(j, reqd_sum, nums):
            k = len(nums)-1
            result = []
            
            while j<k:
                if nums[j]+nums[k] == reqd_sum:
                    result.append([nums[j], nums[k]])
                    j+=1
                    k-=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
                    while nums[k] == nums[k+1] and j<k:
                        k-=1
                elif nums[j]+nums[k]<reqd_sum:
                    j+=1
                else:
                    k-=1
                
            return result
            
            
            
        result = []
        for i, num in enumerate(nums):
            if i>0 and nums[i-1] == num:
                continue
            for res in find_two_sum(i+1, -1*num, nums):
                res = res + [num]
                result.append(res)
            
        return result
        
            