class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_to_number = {"I":1, "V":5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
        
        curr = s[0]
        result = 0
        
        for char in s[1:]:
            if roman_to_number[char]<=roman_to_number[curr]:
                result+=roman_to_number[curr]
            else:
                result-=roman_to_number[curr]
            curr = char
        
        result+=roman_to_number[curr]
        return result
                
        
        