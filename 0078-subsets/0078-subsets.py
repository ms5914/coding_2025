class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        result = []
        
        def find_subsets(index, current_subset):
            if index == len(nums):
                result.append(list(current_subset))
            else:
                current_subset.append(nums[index])
                find_subsets(index+1, current_subset)
                current_subset.pop()
                find_subsets(index+1, current_subset)
        
        find_subsets(0, [])
        return result
        
            
        