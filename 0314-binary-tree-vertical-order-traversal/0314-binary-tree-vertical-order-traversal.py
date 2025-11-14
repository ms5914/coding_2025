# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0
        queue = deque([(root, 0)])
        columnTable[0].append(root.val)

        while queue:
            node, column = queue.popleft()
            min_column = min(min_column, column)
            max_column = max(max_column, column)        
            if node.left:
                columnTable[column-1].append(node.left.val)
                queue.append((node.left, column - 1))
            if node.right:
                columnTable[column+1].append(node.right.val)
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in range(min_column, max_column + 1)]
        