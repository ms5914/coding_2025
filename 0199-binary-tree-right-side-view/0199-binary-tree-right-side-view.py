# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        if not root:
            return []

        q = deque()
        q.append((root, 0))
        result = []

        while q:
            l = len(q)
            root = None
            for i in range(l):
                root, val = q.popleft()
                if root.left:
                    q.append((root.left, val+1))
                if root.right:
                    q.append((root.right, val+1))

            result.append(root.val)
        return result
            
        