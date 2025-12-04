class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[low]: 
                if target <= nums[mid] and target>=nums[low]:
                    high = mid-1
                else:
                    low = mid+1
            elif nums[mid]<=nums[high]:
                if target <= nums[high] and target>=nums[mid]:
                    low = mid+1
                else:
                    high = mid-1
        return -1
            
        
        # [5, 1, 3]
