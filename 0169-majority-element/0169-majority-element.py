class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = nums[0]
        count = 1
        
        for num in nums[1:]:
            if num == ele:
                count+=1
            else:
                count-=1
                if count==0:
                    count = 1
                    ele = num
        return ele
        
        