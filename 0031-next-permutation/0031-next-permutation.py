class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        def reverse(nums, start, end):
            while start<end:
                swap(nums, start, end)
                start+=1
                end-=1
        
        j = len(nums)-1
        while j>0 and nums[j-1]>=nums[j]:
            j-=1

        j-=1
        if j>=0:
            i = len(nums)-1
            while nums[i]<=nums[j]:
                i-=1
            swap(nums, i, j)
        reverse(nums, j+1, len(nums)-1)
        return nums
        


        