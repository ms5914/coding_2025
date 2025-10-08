class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        result = []
        prev_row = [1]
        result.append(prev_row)
        
        for i in range(1, numRows):
            curr_row = [0 for k in range(i+1)]
            curr_row[0] = 1
            for j in range(1, i):
                curr_row[j] =  prev_row[j-1]+prev_row[j]
            curr_row[i] = 1
            result.append(curr_row)
            prev_row = curr_row
        return result
                
            
        