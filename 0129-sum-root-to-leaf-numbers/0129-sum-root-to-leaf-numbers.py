# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
       
        def find_number(root, number):
            nonlocal result
            if not root:
                return
            number = number*10+root.val
            if not root.left and not root.right:
                result+=number
            else:
                find_number(root.left, number)
                find_number(root.right, number)
        
        find_number(root, 0)
        return result
            
            