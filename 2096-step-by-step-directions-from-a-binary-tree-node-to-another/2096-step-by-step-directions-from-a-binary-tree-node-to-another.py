# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:


        def find_lcs(node, val1, val2):
            if node.val == val1 or node.val == val2:
                return node
            else:
                node1, node2 = None, None
                if node.left:
                    node1 = find_lcs(node.left, val1, val2)
                if node.right:
                    node2 = find_lcs(node.right, val1, val2)
            
            if node1 and node2:
                return node
            else:
                return node1 or node2

        def find_direction(node, val):
            if not node:
                return
            q = deque()
            q.append((node, ""))
            while q:
                node, path = q.popleft()
                if node.val == val:
                    return path
                if node.left:
                    q.append((node.left, path+"L"))
                if node.right:
                    q.append((node.right, path+"R"))
                   
                
            

    
        lcs_node = find_lcs(root, startValue, destValue)
        directions1 = find_direction(lcs_node, startValue)
        directions2 = find_direction(lcs_node, destValue)

        result = []
        for direction in directions1:
            result.append("U")
        
        return "".join(result)+directions2


        