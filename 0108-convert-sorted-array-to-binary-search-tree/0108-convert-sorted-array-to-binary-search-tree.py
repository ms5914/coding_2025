# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None
        
        size = len(nums)
        middle_element = size//2
        
        root = TreeNode(nums[middle_element])
        root.left = self.sortedArrayToBST(nums[:middle_element])
        root.right = self.sortedArrayToBST(nums[middle_element+1:])
        
        return root
        