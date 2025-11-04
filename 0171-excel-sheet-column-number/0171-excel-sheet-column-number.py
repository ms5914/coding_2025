class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        #this is base 26 conversion to base 10. 
        columnNumber = 0
        for ch in columnTitle:
            columnNumber = columnNumber*26+(ord(ch)-ord("A")+1)
        return columnNumber
            
        