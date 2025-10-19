# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        curr_index = 0
        
        def node_index(inorder):
            val_ind = {}
            for ind, val in enumerate(inorder):
                val_ind[val] = ind
            return val_ind
        
        
        
        #the only usage of inorder is to make sure it is not empty for the current subtree, the next node will always be the current index in preorder array. We need nonlocal var to track that curr_index across recursions. 
        def build(left, right):
            nonlocal curr_index
            
            if left>right:
                return None
            
           
            val = preorder[curr_index]
            root = TreeNode(preorder[curr_index])
            curr_index+=1
            partition = mapp[val]
            root.left = build(left, partition-1)
            root.right = build(partition+1, right)
            return root
        
        
        mapp = node_index(inorder)
        return build(0, len(inorder)-1)
        
        
        
        
        