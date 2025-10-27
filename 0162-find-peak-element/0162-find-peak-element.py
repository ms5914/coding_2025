class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def find_peak(l, r):
            
            mid = l+(r-l)//2
            left = nums[mid-1] if mid-1>=0 else -1*float("inf")
            right = nums[mid+1] if mid+1 < len(nums) else -1*float("inf")
            if nums[mid] > left and nums[mid] > right:
                return mid
            elif nums[mid] < right:
                return find_peak(mid+1, r)
            else:
                return find_peak(l, mid-1)
        
        return find_peak(0, len(nums)-1)