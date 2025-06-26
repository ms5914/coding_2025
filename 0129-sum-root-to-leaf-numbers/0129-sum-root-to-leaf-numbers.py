# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def find_sum(root, curr_list):
            if not root:
                return 0    

            if not root.left and not root.right:
                return int(''.join(curr_list+[str(root.val)]))
            
            return find_sum(root.left, curr_list+[str(root.val)])+find_sum(root.right, curr_list+[str(root.val)])
        
        return find_sum(root, [])
        # result = 0
        # curr_sum = 0

        # def find_sum(root, curr_sum):
        #     if not root:
        #         return curr_sum
            
        #     else:
        #         s = 0
        #         if root.left:
        #             s+ind_sum(root.left, curr_sum*10+root.val) + find_sum(root.right, curr_sum*10+root.val)
        
        # return find_sum(root, 0)
            
        