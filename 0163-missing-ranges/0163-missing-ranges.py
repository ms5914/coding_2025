class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        
        for num in nums:
            if num>lower:
                result.append([lower, num-1])
                lower = num+1
            else:
                lower+=1
        
        if lower<=upper:
            result.append([lower, upper])
        return result
                
        