class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        index = -1
        
        def find_position(nums, start, end, first_occurence):
            nonlocal index
            if start>end:
                return
            mid = start+(end-start)//2
            if nums[mid] == target:
                index = mid
                if not first_occurence:
                    find_position(nums, mid+1, end, first_occurence)
                else:
                    find_position(nums, start, mid-1, first_occurence)
            elif nums[mid] < target:
                find_position(nums, mid+1, end, first_occurence)
            else:
                find_position(nums, start, mid-1, first_occurence)
        
        
        result = []
        find_position(nums, 0, len(nums)-1, True)
        result.append(index)
        
        index = -1
        find_position(nums, 0, len(nums)-1, False)
        result.append(index)
        
        return result
        
        
                
        