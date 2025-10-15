# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        if not root:
            return result
        
        current = root
        while current:
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                temp = current.left
                while temp.right and temp.right != current:
                    temp = temp.right
                
                if not temp.right:
                    temp.right = current
                    current = current.left
                
                else:
                    result.append(current.val)
                    temp.right = None
                    current = current.right
        
        return result