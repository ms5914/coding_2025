# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        diameter = 0
        def find_max_len(root):
            if not root :
                return 0
            else:
                nonlocal diameter
                left_max = find_max_len(root.left)
                right_max = find_max_len(root.right)
                diameter = max(diameter, left_max+right_max)
            return max(left_max, right_max)+1
        
        find_max_len(root)
        return diameter

        