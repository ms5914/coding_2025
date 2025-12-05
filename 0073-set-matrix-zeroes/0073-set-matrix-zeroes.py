class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])
        is_col_zero = False

        for i in range(m):
            if matrix[i][0] == 0:
                is_col_zero = True
        
        for i in range(n):
            if matrix[0][i] == 0:
                matrix[0][0] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for k in range(n):
                    matrix[i][k] = 0
        
        for i in range(1, n):
            if matrix[0][i] == 0:
                for k in range(m):
                    matrix[k][i] = 0
        
        if matrix[0][0] == 0:
            for i in range(0, n):
                matrix[0][i] = 0
        
        if is_col_zero:
            for i in range(0, m):
                matrix[i][0] = 0
        
        return matrix


        



        
        