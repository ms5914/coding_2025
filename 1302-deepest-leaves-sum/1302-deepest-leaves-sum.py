# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_depth = -1
        total = 0

        def dfs(node, depth):
            nonlocal max_depth
            nonlocal total
            if not node:
                return 0
            
            if not node.left and not node.right:
                if depth > max_depth:
                    max_depth = depth
                    total = node.val
                elif depth == max_depth:
                    total+=node.val
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return total
        