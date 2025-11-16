class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        ptr = 1
        for num in nums[1:]:
            if prev == num:
                continue
            else:
                nums[ptr] = num
                prev = num
                ptr+=1
        
        return ptr

        