# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        
        min_key = float("inf")
        max_key = float("-inf")
        hm = defaultdict(list)

        q = deque()
        q.append((0, root))
        while q:
            index, node = q.popleft()
            min_key = min(min_key, index)
            max_key = max(max_key, index)
            hm[index].append(node.val)
            if node.left:
                q.append((index-1, node.left))
            if node.right:
                q.append((index+1, node.right))
        
        for key in range(min_key, max_key+1):
            if key in hm:
                result.append(hm[key])
        return result

            



        