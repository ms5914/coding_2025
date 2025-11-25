# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
      #preorder traversal

      result = 0
      curr_num = 0
      
      while root:
        if not root.left:
            curr_num = curr_num*10+root.val
            if root.right is None:
                result += curr_num
            root = root.right
        else:
            root_left = root.left
            step = 1
            while root_left.right and root_left.right != root:
                root_left = root_left.right
                step+=1
            
            if root_left.right == root:
                root_left.right = None
                if not root_left.left:
                    result+=curr_num
                root = root.right
                for i in range(step):
                    curr_num //= 10
                
            else:
                root_left.right = root
                curr_num = curr_num*10+root.val
                root = root.left
                
      return result
        




            
            