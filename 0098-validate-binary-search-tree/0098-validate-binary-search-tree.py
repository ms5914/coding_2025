# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def isValid(node, min_val, max_val):
            if not node:
                return True
            
            if node.val > min_val and node.val < max_val:
                return isValid(node.left, min_val, node.val) and isValid(node.right, node.val, max_val)
            
            return False
        
        return isValid(root, -1*float("inf"), float("inf"))
        