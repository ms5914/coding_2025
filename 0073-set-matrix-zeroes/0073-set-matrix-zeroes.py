class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        is_row = False
        is_col = False
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    if i == 0: 
                        is_row = True
                    if j == 0:
                        is_col = True
        
        
        for r in range(1,n):
            if matrix[0][r] == 0:
                for s in range(m):
                    matrix[s][r] = 0
                    
        for k in range(1,m):
            if matrix[k][0] == 0:
                for l in range(n):
                    matrix[k][l] = 0
        if is_row:
            for p in range(n):
                matrix[0][p] = 0
        if is_col:
            for q in range(m):
                matrix[q][0] = 0
        
            
                    
                