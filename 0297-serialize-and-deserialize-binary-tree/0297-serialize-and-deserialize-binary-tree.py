# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        q = deque()
        q.append(root)
        nodes_list = []
        nodes_list.append(str(root.val))
        while q:
            root = q.popleft()
            if root.left:
                nodes_list.append(str(root.left.val))
                q.append(root.left)
            else:
                nodes_list.append("#")
            
            if root.right:
                nodes_list.append(str(root.right.val))
                q.append(root.right)
            else:
                nodes_list.append("#")
        return ",".join(nodes_list)
            
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if len(data) == 0:
            return None
        
        nodes_list = data.split(",")
        index = 0
        root = TreeNode(nodes_list[index]) 
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            
            index+=1
            node.left = TreeNode(nodes_list[index]) if nodes_list[index] != "#" else None
            if node.left: 
                q.append(node.left)
            
            index+=1
            node.right = TreeNode(nodes_list[index]) if nodes_list[index] != "#" else None
            if node.right:
                q.append(node.right)
        
        return root
                
        
            
            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))