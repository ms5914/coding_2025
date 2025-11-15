"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        headA = p
        headB = q

        while headA != headB:
            headA = headA.parent if headA.parent else q
            headB = headB.parent if headB.parent else p
        
        return headA
        