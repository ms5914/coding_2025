# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        left_lca, right_lca = None, None
        if root.val == p.val or root.val == q.val:
            return root
        if root.left:
            left_lca = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right_lca = self.lowestCommonAncestor(root.right, p, q)
        
        if left_lca and right_lca:
            return root
            
        return left_lca or right_lca
        

        