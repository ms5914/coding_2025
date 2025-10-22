# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        # if p.right:
        #     temp = p.right
        #     while temp.left:
        #         temp = temp.left
        #     return temp
        

        #It's very similar to binary search remember that.
        succ = None
        def find_successor(root, p):
            if not root:
                return
            
            nonlocal succ
            if root.val <= p.val:
                find_successor(root.right, p)
            else:
                succ = root
                find_successor(root.left, p)
        
        find_successor(root, p)
        return succ
            
        