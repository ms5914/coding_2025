# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0
        if not root:
            return 0
        def find_longest_path(root):
            max_left_path, max_right_path = 0,0
            if root.left:
                max_left_path = find_longest_path(root.left)
            if root.right:
                max_right_path = find_longest_path(root.right)
            
            nonlocal diameter
            diameter = max(diameter, max_left_path+max_right_path)
            
            return max(max_left_path,max_right_path)+1
        
        find_longest_path(root)
        return diameter
            

        