"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        
        #recursive approach
        def connect_next(dummy):
            if not dummy:
                return
            temp = dummy
            dummy2 = Node()
            while temp:
                if dummy2:
                    dummy2.next = temp.left
                    dummy2 = dummy2.next
                if dummy2:
                    dummy2.next = temp.right
                    dummy2 = dummy2.next
                temp = temp.next
            connect_next(dummy.left)
        
        connect_next(root)
        return root
            
             
            
         
        #iterative approach
        # dummy = root
        # while dummy:
        #     temp = dummy
        #     dummy2 = Node()
        #     while temp:
        #         if dummy2:
        #             dummy2.next = temp.left
        #             dummy2 = dummy2.next
        #         if dummy2:
        #             dummy2.next = temp.right
        #             dummy2 = dummy2.next
        #         temp = temp.next
        #     dummy = dummy.left 
        # return root
            
                
                