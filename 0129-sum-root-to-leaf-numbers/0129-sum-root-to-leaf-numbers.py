# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        result = 0

        def find_sum(root, curr_sum):
            
            nonlocal result
            if not root.left and not root.right:
                result+=curr_sum
            else:
                if root.left:
                    find_sum(root.left, curr_sum*10+root.left.val)
                if root.right:
                    find_sum(root.right, curr_sum*10+root.right.val)
            
        find_sum(root, root.val)
        return result
                
        