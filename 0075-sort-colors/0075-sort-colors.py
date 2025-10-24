class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero, curr, two = 0, 0, len(nums)-1
        
        while curr<=two:
            if nums[curr] == 0:
                nums[zero], nums[curr] = nums[curr], nums[zero]
                zero+=1
                curr+=1
            elif nums[curr] == 1:
                curr+=1
            else:
                nums[curr], nums[two] = nums[two], nums[curr]
                two-=1
        return nums
                
        