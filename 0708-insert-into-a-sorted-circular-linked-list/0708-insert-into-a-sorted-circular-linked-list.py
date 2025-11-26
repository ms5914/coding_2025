"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        if not head:
            temp1 = Node(insertVal, None)
            temp1.next = temp1
            return temp1
        prev = head
        curr = head.next
        insert = False
        while curr != head:
            if insertVal >= prev.val and insertVal <= curr.val:
                insert = True
                break
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    insert = True
                    break
            prev = curr
            curr = curr.next

        new_node = Node(insertVal, curr)
        prev.next = new_node
        return head
                
                


        
        