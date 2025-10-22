class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
            
        result = []
        
        def find_permutation(nums, index):
            if index == len(nums):
                result.append(list(nums))
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                find_permutation(nums, index+1)
                nums[i], nums[index] = nums[index], nums[i]
        find_permutation(nums, 0)
        return result



    
        