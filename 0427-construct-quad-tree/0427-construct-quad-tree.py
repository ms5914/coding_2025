"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        # print(grid)
        if n > 0:
            prev = grid[0][0]
            node = Node(prev, False, None, None, None, None)
            if all([prev == grid[i][j] for i in range(n) for j in range(n)]):
                node.isLeaf = True
                return node
            else:
                mid_row, mid_col = n // 2, n //2
                node.topLeft = self.construct([row[:mid_col] for row in grid[:mid_row]])
                node.topRight = self.construct([row[mid_col:] for row in grid[:mid_row]])
                node.bottomLeft = self.construct([row[:mid_col] for row in grid[mid_row:]])
                node.bottomRight = self.construct([row[mid_col:] for row in grid[mid_row:]])
                return node
        return
            

                
                
    

        