class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        for idx, num in enumerate(digits[::-1]):
            if num == 9:
                digits[n-idx-1] = 0
            else:
                digits[n-idx-1]+=1
                return digits
        
        return [1]+digits

        