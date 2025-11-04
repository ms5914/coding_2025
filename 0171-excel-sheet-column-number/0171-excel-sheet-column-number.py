class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnNumber = 0
        for ch in columnTitle:
            columnNumber = columnNumber*26+(ord(ch)-ord("A")+1)
        return columnNumber
            
        