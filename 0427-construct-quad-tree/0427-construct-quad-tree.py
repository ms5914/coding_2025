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
        def solve(x1, y1, length):
            # Return a leaf node if the matrix size is one
            if length == 1:
                return Node(grid[x1][y1] == 1, True)
            
            # Recursive calls to the four sub-matrices
            half = length // 2
            top_left = solve(x1, y1, half)
            top_right = solve(x1, y1 + half, half)
            bottom_left = solve(x1 + half, y1, half)
            bottom_right = solve(x1 + half, y1 + half, half)
            
            # If all four nodes are leaves with the same value, merge them
            if (top_left.isLeaf and top_right.isLeaf and 
                bottom_left.isLeaf and bottom_right.isLeaf and
                top_left.val == top_right.val == bottom_left.val == bottom_right.val):
                return Node(top_left.val, True)
            
            # Otherwise return a non-leaf node with children
            return Node(False, False, top_left, top_right, bottom_left, bottom_right)
        
        return solve(0, 0, len(grid))
            

                
                
    

        