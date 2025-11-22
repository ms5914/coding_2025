class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row, col = 0, 0
        m, n = len(mat), len(mat[0])

        result = []
        up, down = True , False

        while row < m and col < n:
            result.append(mat[row][col])

            if up:
                if row-1 >= 0 and col+1<n:
                    row = row-1
                    col = col+1
                elif col+1< n:
                    col= col+1
                    up = False
                    down = True
                else:
                    row = row+1
                    up = False
                    down = True
            elif down:
                if row+1 < m and col-1 >= 0:
                    row = row+1
                    col = col-1
                elif row+1< m:
                    row= row+1
                    down = False
                    up = True
                else:
                    col = col+1
                    up = True
                    down = False
        return result



        