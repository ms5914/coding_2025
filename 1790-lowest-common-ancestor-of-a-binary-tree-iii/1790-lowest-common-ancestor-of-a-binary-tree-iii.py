"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        if p == q:
            return p
        headA = p
        headB = q

        while p != q:
            p = p.parent or headB
            q = q.parent or headA
        return p

            

        
        