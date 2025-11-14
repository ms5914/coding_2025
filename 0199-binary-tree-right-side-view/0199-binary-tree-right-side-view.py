# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        q.append(root)
        result = []
        while q:
            num = len(q)
            ele = None
            for i in range(num):
                ele = q.popleft()
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
            if ele:
                result.append(ele.val)
        return result
        


        