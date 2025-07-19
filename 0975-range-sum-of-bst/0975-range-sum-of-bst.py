# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        
        
        def find_sum(root):
            if not root:
                return 0
            range_sum = 0
            if root.val <= high and root.val >= low:
                range_sum+=root.val
            range_sum+=find_sum(root.left)
            range_sum+=find_sum(root.right)
            return range_sum
        
        return find_sum(root)
        

            
                
        